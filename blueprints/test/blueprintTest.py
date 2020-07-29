from flask import Blueprint, render_template

test = Blueprint("blueprintTest", __name__, static_folder="static", template_folder="templates")

@test.route("/")
def blueprintTest():
    return "<h1>Blueprint Test</h1>"