#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ outputs “Welcome to Holberton” as page title (<title>) and
    “Hello world” as header (<h1>).
    """
    return render_template('0-index.html')
