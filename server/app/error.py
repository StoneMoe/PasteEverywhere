#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import getLogger

from flask import request

from app.utils import APICode, api_body, get_real_ip

logger = getLogger(__name__)


def register_all_to(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return "Forbidden", 403

    @app.errorhandler(404)
    def page_not_found(error):
        return "Not Found", 404

    @app.errorhandler(500)
    def server_error_page(error):
        return "Error", 500

    @app.errorhandler(429)
    def too_many_request(error):
        is_api = request.path.startswith('/api')
        if is_api:
            logger.warning('Blocking IP: %s' % get_real_ip())
            return api_body(APICode.ERR, message='Too fast')
        else:
            return 'Internal Error', 500
