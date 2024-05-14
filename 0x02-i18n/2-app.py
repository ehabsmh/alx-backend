#!/usr/bin/env python3
"""2. Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """matches with the requested language"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """hello world"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
