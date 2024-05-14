#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
