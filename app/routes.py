from app import app
from flask import render_template

"""
if request in ("http://dii.tj/", "http://dii.tj/index", 1)":
    return "Hello World!"

"""

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/')
@app.route('/dii')
def dii_special_hello_msg():
    return "Salam, Aleykum!"


@app.route('/main')
def main_page():
    title = "DII Coolest WebSide Ever Existed in this  Universe  and in other Multiverses"
    user = {
        "username": "Omina"
    }

    return render_template(
        template_name_or_list="index.html",
        title=title,
        user=user,
    )
