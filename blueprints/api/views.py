from flask import Blueprint, jsonify
from utils import *


api_blueprint = Blueprint('api', __name__, url_prefix='/api/')


@api_blueprint.route('/posts/')
def api_posts_page():
    """ Представление списка постов
    """
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/posts/<int:post_id>')
def api_post_by_id_page(post_id):
    """ Представление поста по идентификатору
    """
    post = get_posts_by_pk(post_id)
    return jsonify(post)
