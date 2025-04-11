from app import app
from flask import render_template
from app.forms import LoginForm

"""
if request in ("http://dii.tj/", "http://dii.tj/index", 1)":
    return "Hello World!"

"""

@app.route('/')
def index():
    return render_template('index.html')


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


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
