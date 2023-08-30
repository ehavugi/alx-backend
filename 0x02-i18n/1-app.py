#!/usr/bin/env python3
"""
Main app page. First app in series about localization
and internationalization
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """Config language support
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def main():
    """
    App route. Main page
    Render tempalte 0-index.html
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(port=8091)
