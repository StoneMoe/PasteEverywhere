#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
