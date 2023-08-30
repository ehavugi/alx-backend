#!/usr/bin/env python3
"""
Main app page. First app in series about localization
and internationalization
"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request
from flask import g


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
username = None


def get_user():
    """Return a user ID given a the request.
    """
    user_id = request.args.get('login_as', None)
    try:
        if user_id:
            user = users.get(int(user_id), None)
            if user:
                return user.get('name', None)
    except ValueError:
        return None


@app.before_request
def before_request():
    """
    """
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@app.route("/")
def main():
    """
    App route. Main page
    Render template 5-index.html
    """
    username = g.user
    return render_template("5-index.html", username=g.user)


@babel.localeselector
def get_locale():
    """Local getter function using babel.
    can be force to a locale by parameter.
    """
    req = request.args.get("locale", "")
    # First Option: local from url
    if req in app.config['LANGUAGES']:
        return req
    # Second option: Locale from user parameters
    if g.user:
        user_id = request.args.get('login_as', None)
        try:
            option2 = users.get(int(user_id))['locale']
            if option2 in app.config['LANGUAGES']:
                return option2
        except ValueError:
            pass
    # Option 3: Locale from request headers
    locale = request.headers.get('Accept-Language', None)
    if locale in app.config['LANGUAGES']:
        return locale
    # Option 4: Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(port=8091, debug=True)
