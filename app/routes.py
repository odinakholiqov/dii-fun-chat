from app import app


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
