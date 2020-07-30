from flask import Blueprint, render_template

add = Blueprint("budget", __name__, static_folder="static", template_folder="templates")

@add.route("/add")
def addition():
    return "<h1>Blueprint Test</h1>"