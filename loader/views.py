from flask import Blueprint, render_template, request

from functions import save_picture, add_post
from menu import menu

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def form_post_page():
    return render_template('post_form.html', menu=menu)


@loader_blueprint.route('/post', methods=['POST'])
def upload_post_page():
    pic = request.files.get('picture')
    content = request.form.get('content')

    if not pic or not content:
        return 'ошибка добавления поста.'

    picture_path = '/' + save_picture(pic)
    post = add_post({'pic': picture_path, 'content': content})

    return render_template('post_uploaded.html', menu=menu, post=post)
