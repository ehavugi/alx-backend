#!/usr/bin/env python3
"""
Main app page. First app in series about localization
and internationalization
"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config language support
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Return a user ID given a the request.
    """
    user_id = request.args.get('login-as', None)
    return users.get(user_id, None)


@app.before_request
def before_request():
    """
    """
    user = get_user()
    if user:
        flask.g.user = user


@app.route("/")
def main():
    """
    App route. Main page
    Render template 5-index.html
    """
    return render_template("5-index.html")


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
