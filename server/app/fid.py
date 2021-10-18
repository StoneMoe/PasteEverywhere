from app import redis
from app.utils import rand_str


class FIDService:
    """File ID Service"""

    @staticmethod
    def gen_fid(length):
        conflict = True
        fid = None
        for _ in range(15):
            fid = rand_str(length)
            if redis.exists(fid) == 0:
                conflict = False
                break
        if conflict:
            return None
        else:
            return fid
