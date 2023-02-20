from flask import Blueprint, render_template, request
from utils import *


main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/')
def index_page():
    """ Представление ленты постов
    """
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:postid>')
def post_by_id_page(postid):
    """ Представление поста по идентификатору
    """
    post = get_posts_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search/', methods=['GET'])
def search_page():
    """ Представление поиска постов по ключевому слову
    """
    s = request.args.get('s')
    query_posts = search_for_posts(s)[:10]
    return render_template('search.html', posts=query_posts)


@main_blueprint.route('/users/<username>', methods=['GET'])
def users_page(username):
    """ Представление постов пользователя
    """
    user_posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts)
