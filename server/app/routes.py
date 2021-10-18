import io
import pickle

from flask import request
from flask import send_file, Response

from app import redis, limiter
from app.fid import FIDService
from app.utils import APICode, api_body


def register_all_to(app):
    @app.route('/')
    def api_home():
        return api_body(APICode.OK)

    @app.route('/upload', methods=['POST'])
    @limiter.limit('1500/day;1000/hour;40/minute')
    def api_upload():
        body = request.get_json(force=True, silent=True) or dict()

        text = body.get('text', None)
        file = request.files

        if text is not None and text:
            fid = FIDService.gen_fid(5)
            if fid is None:
                return api_body(APICode.ERR, message='服务繁忙，请稍后再试')

            redis.set(fid, pickle.dumps(
                {
                    'text': text
                }
            ), 15 * 60)  # 15 min expire
            return api_body(APICode.OK, data=fid)
        elif file is not None:
            fid = FIDService.gen_fid(5)
            if fid is None:
                return api_body(APICode.ERR, message='服务繁忙，请稍后再试')
            if file['file'].content_length > 1:
                return api_body(APICode.ERR, message='文件过大')
            redis.set(fid, pickle.dumps(
                {
                    'name': file['file'].filename,
                    'bytes': io.BytesIO(
                        file['file'].stream.read()
                    ).getvalue()
                }
            ), 15 * 60)

            return api_body(APICode.OK, data=fid)
        else:
            return api_body(APICode.ERR)

    @app.route('/s/<string:fid>')
    def api_home(fid):
        if redis.exists(fid) != 1:
            return '链接有误'
        else:
            data = pickle.loads(redis.get(fid))
            if 'text' in data:
                return Response(data['text'], mimetype='text/plain')
            else:
                return send_file(io.BytesIO(data['bytes']),
                                 mimetype='application/octet-stream',
                                 as_attachment=True,
                                 attachment_filename=data['name'],
                                 cache_timeout=15 * 60)
