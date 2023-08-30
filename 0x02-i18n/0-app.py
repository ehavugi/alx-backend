#!/usr/bin/env python3
"""
Main app page. First app in series about localization
and internationalization
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    """
    App route. Main page.
    Render tempalte 0-index.html
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(port=8091)
