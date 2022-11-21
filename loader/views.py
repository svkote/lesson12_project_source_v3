import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort

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
    if pic.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info(f'Загруженный файл не картинка - {pic.filename}')
        return 'неверный формат файла. должен быть jpeg или png'

    try:
        picture_path = '/' + save_picture(pic)
    except FileNotFoundError:
        logging.error('Файл не найден')
        abort(404)
    except JSONDecodeError:
        return "Ошибка в файле JSON"
    post = add_post({'pic': picture_path, 'content': content})

    return render_template('post_uploaded.html', menu=menu, post=post)
