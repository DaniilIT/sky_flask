from flask import Blueprint, render_template, request, redirect
from .dao.posts_dao import PostsDAO
from .dao.comments_dao import CommentsDAO
from .dao.bookmarks_dao import BookmarksDAO
import config


main_blueprint = Blueprint('main', __name__, template_folder='templates')

posts_dao = PostsDAO(config.POSTS_JSON_PATH)
comments_dao = CommentsDAO(config.COMMENTS_JSON_PATH)
bookmarks_dao = BookmarksDAO(config.BOOKMARKS_JSON_PATH)


@main_blueprint.route('/')
def index_page():
    """ Представление ленты постов
    """
    posts = posts_dao.get_all()
    bookmarks = bookmarks_dao.get_all()
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@main_blueprint.route('/posts/<int:post_id>')
def post_by_id_page(post_id):
    """ Представление поста по идентификатору
    """
    post = posts_dao.get_by_pk(post_id)
    comments = posts_dao.get_comments_by_post_id(post_id, comments_dao)
    bookmarks = bookmarks_dao.get_all()
    return render_template('post.html', post=post, comments=comments, bookmarks=bookmarks)


@main_blueprint.route('/search/', methods=['GET'])
def search_page():
    """ Представление поиска постов по ключевому слову
    """
    s = request.args.get('s')
    query_posts = posts_dao.search(s)[:10]
    bookmarks = bookmarks_dao.get_all()
    return render_template('search.html', posts=query_posts, bookmarks=bookmarks)


@main_blueprint.route('/users/<username>')
def users_page(username):
    """ Представление постов пользователя
    """
    user_posts = posts_dao.get_by_user(username)
    bookmarks = bookmarks_dao.get_all()
    return render_template('user-feed.html', posts=user_posts, bookmarks=bookmarks)


@main_blueprint.route('/bookmarks/add/<int:post_id>')
def add_mark_page(post_id):
    """ Представление добавления поста в закладки
    """
    post = posts_dao.get_by_pk(post_id)
    bookmarks_dao.add_bookmark(post)
    return redirect('/', code=302)


@main_blueprint.route('/bookmarks/remove/<int:post_id>')
def remove_mark_page(post_id):
    """ Представление удаления поста в закладки
    """
    post = posts_dao.get_by_pk(post_id)
    bookmarks_dao.remove_bookmark(post)
    return redirect('/', code=302)


@main_blueprint.route('/bookmarks/')
def bookmarks_page():
    """ Представление удаления поста в закладки
    """
    bookmarks_posts = bookmarks_dao.get_all()
    return render_template('bookmarks.html', posts=bookmarks_posts)
