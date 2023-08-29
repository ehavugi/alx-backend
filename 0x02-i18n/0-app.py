#!/usr/bin/env python3
"""
Main app page
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    """
    App route. Main page
    """
    title = "Welcome to Holberton"
    header = "Hello world"
    return render_template("0-index.html", title=title, header=header)


if __name__ == '__main__':
    app.run(port=80)
