from flask import Flask, request, render_template, send_from_directory

# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

menu = [
    {'url': '/', 'title': 'Главная'},
    {'url': '/post', 'title': 'Добавить пост'},
]


@app.route("/")
def page_index():
    """ главная страница (поиск постов)"""
    # s = request.args['s']
    return render_template('index.html', menu=menu)


@app.route("/list")
def page_tag():
    """страничка ленты по тегу"""
    return render_template('post_list.html', menu=menu)


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    """страничка добавления поста"""
    return render_template('post_form.html', menu=menu)


@app.route("/post", methods=["POST"])
def page_post_upload():
    """страничка после добавления поста"""
    return render_template('post_uploaded.html', menu=menu)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
