from flask import Blueprint, jsonify
from blueprints.main.dao.posts_dao import PostsDAO
from .logger import Logger
import config


api_blueprint = Blueprint('api', __name__, url_prefix='/api/')

posts_dao = PostsDAO(config.POSTS_JSON_PATH)

api_logger = Logger('api_log.log')


@api_blueprint.route('/posts/')
def api_posts_page():
    """ Представление списка постов
    """
    api_logger.record_info('/api/posts')
    posts = posts_dao.get_all()
    return jsonify([post.get_post_dict() for post in posts])


@api_blueprint.route('/posts/<int:post_id>')
def api_post_by_id_page(post_id):
    """ Представление поста по идентификатору
    """
    api_logger.record_info(f'/api/posts/{post_id}')
    post = posts_dao.get_by_pk(post_id)
    return jsonify(post.get_post_dict())
