from flask import Blueprint, jsonify
from blueprints.main.dao.posts import Post, PostsDAO
from blueprints.api.logger import Logger


api_blueprint = Blueprint('api', __name__, url_prefix='/api/')

posts_dao = PostsDAO()

api_logger = Logger('api_log.log')


@api_blueprint.route('/posts/')
def api_posts_page():
    """ Представление списка постов
    """
    api_logger.record_info('/api/posts')
    posts = posts_dao.get_all()
    return jsonify([Post.get_post_dict(post) for post in posts])


@api_blueprint.route('/posts/<int:post_id>')
def api_post_by_id_page(post_id):
    """ Представление поста по идентификатору
    """
    api_logger.record_info(f'/api/posts/{post_id}')
    post = posts_dao.get_by_pk(post_id)
    return jsonify(Post.get_post_dict(post))
