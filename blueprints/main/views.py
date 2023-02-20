from flask import Blueprint, render_template, request
from blueprints.main.dao.posts import PostsDAO


main_blueprint = Blueprint('main', __name__, template_folder='templates')

posts_dao = PostsDAO()


@main_blueprint.route('/')
def index_page():
    """ Представление ленты постов
    """
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:postid>')
def post_by_id_page(postid):
    """ Представление поста по идентификатору
    """
    post = posts_dao.get_by_pk(postid)
    comments = posts_dao.get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search/', methods=['GET'])
def search_page():
    """ Представление поиска постов по ключевому слову
    """
    s = request.args.get('s')
    query_posts = posts_dao.search(s)[:10]
    return render_template('search.html', posts=query_posts)


@main_blueprint.route('/users/<username>', methods=['GET'])
def users_page(username):
    """ Представление постов пользователя
    """
    user_posts = posts_dao.get_by_user(username)
    return render_template('user-feed.html', posts=user_posts)
