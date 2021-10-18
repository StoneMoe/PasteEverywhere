#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import getLogger

from flask import Flask
from flask_limiter import Limiter
from flask_redis import FlaskRedis

from app.utils import get_real_ip

logger = getLogger(__name__)

redis = FlaskRedis()
limiter = Limiter(key_func=get_real_ip)


def create_app():
    app = Flask(__name__)

    from app import config
    app.config.from_object(config)

    from app import error
    error.register_all_to(app)

    from app import routes

    # Plugins
    redis.init_app(app)
    limiter.init_app(app)

    return app
