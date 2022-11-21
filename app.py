import logging

from flask import Flask, request, render_template, send_from_directory

from loader.views import loader_blueprint
from main.views import main_blueprint
from menu import menu

# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.errorhandler(404)
def PageNotFound(error):
    return render_template('page404.html', menu=menu)


@app.errorhandler(500)
def PageNotFound(error):
    return render_template('page500.html', menu=menu)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
