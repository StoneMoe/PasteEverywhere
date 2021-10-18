#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from logging import getLogger

from app.utils import rand_str

logger = getLogger(__name__)


class Config(object):
    SECRET_KEY = rand_str(32)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    REDIS_URL = 'redis://redis:6379/0'
    RATELIMIT_STORAGE_URL = 'redis://redis:6379/1'


_config = {
    'production': Config
}

# Select config from environment variable
choose = os.getenv('FLASK_ENV') or 'production'
# Shortcut
config = _config[choose]

logger.warning('Configuration: %s' % choose)
