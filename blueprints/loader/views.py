import logging
from pathlib import Path

from flask import Blueprint, render_template, request, current_app, abort, send_from_directory

from dao import PostsDAO


loader_blueprint = Blueprint('loader', __name__, template_folder='templates')

posts_dao = PostsDAO()

logger_mine = logging.getLogger('logger')


@loader_blueprint.route('/post/')
def logger_page():
    """ Форма для создания поста
    """
    return render_template('post_form.html')


@loader_blueprint.route('/uploads/<path:path>')
@loader_blueprint.route('/uploads', methods=['POST'])
def uploaded_page(path=None):
    """ Загрузка нового поста методом POST.
    Без метода - рендер
    """
    if request.method == 'POST':
        picture = request.files.get('picture')
        if not picture:
            logger_mine.error('Попытка загрузки неразрешенного типа файла')
        elif picture.filename == '':
            logger_mine.info('Попытка загрузки сообщения без файла')
        elif (Path(picture.filename).suffix.lower()
              not in current_app.config['UPLOAD_EXTENSIONS']):
            logger_mine.info('Попытка загрузки сообщения без файла')
            abort(400)

        picture.save(f'./uploads/{picture.filename}')
        text = request.values.get('content')
        posts_dao.upload({
            'poster_name': 'None',
            'poster_avatar': None,
            'pic': '/uploads/' + picture.filename,
            'content': text,
            'views_count': 0,
            'likes_count': 0,
        })
        return render_template('post_uploaded.html', added_text=text, added_picture=picture.filename)
    else:
        return send_from_directory('uploads', path)