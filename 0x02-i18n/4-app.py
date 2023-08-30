#!/usr/bin/env python3
"""
Main app page. First app in series about localization
and internationalization
"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


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
    Render template 4-index.html
    """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """Local getter function using babel.
    can be force to a locale by parameter.
    """
    req = request.args.get("locale", "")
    if req in app.config['LANGUAGES']:
        return req
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(port=8091)
