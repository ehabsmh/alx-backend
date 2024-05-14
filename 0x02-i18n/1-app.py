#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']

babel = Babel(app, default_locale=Config.LANGUAGES[0], default_timezone='UTC')

