from flask import Blueprint, jsonify
from blueprints.api.logger import Logger
from utils import *


api_blueprint = Blueprint('api', __name__, url_prefix='/api/')

api_logger = Logger('api_log.log')


@api_blueprint.route('/posts/')
def api_posts_page():
    """ Представление списка постов
    """
    api_logger.record_info('/api/posts')
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/posts/<int:post_id>')
def api_post_by_id_page(post_id):
    """ Представление поста по идентификатору
    """
    api_logger.record_info(f'/api/posts/{post_id}')
    post = get_posts_by_pk(post_id)
    return jsonify(post)
