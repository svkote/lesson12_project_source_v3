import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort

from functions import get_posts_by_word
from menu import menu

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """Главная страница (поиск постов)"""
    # s = request.args['s']
    return render_template('index.html', menu=menu)


@main_blueprint.route('/search')
def search_page():
    search_word = request.args.get('s', '')
    logging.info(f'Выполняется поиск по слову {search_word}')
    try:
        posts = get_posts_by_word(search_word)
    except FileNotFoundError:
        abort(404)
    except JSONDecodeError:
        return "Ошибка в файле JSON"
    return render_template('post_list.html', search_word=search_word, posts=posts, menu=menu)
