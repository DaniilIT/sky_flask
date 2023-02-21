from flask import Blueprint, render_template, request, redirect
from blueprints.main.dao.posts import PostsDAO


main_blueprint = Blueprint('main', __name__, template_folder='templates')

posts_dao = PostsDAO()


@main_blueprint.route('/')
def index_page():
    """ Представление ленты постов
    """
    posts = posts_dao.get_all()
    bookmarks = posts_dao.get_bookmarks_all()

    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@main_blueprint.route('/posts/<int:postid>')
def post_by_id_page(postid):
    """ Представление поста по идентификатору
    """
    post = posts_dao.get_by_pk(postid)
    comments = posts_dao.get_comments_by_post_id(postid)
    bookmarks = posts_dao.get_bookmarks_all()
    return render_template('post.html', post=post, comments=comments, bookmarks=bookmarks)


@main_blueprint.route('/search/', methods=['GET'])
def search_page():
    """ Представление поиска постов по ключевому слову
    """
    s = request.args.get('s')
    query_posts = posts_dao.search(s)[:10]
    bookmarks = posts_dao.get_bookmarks_all()
    return render_template('search.html', posts=query_posts, bookmarks=bookmarks)


@main_blueprint.route('/users/<username>')
def users_page(username):
    """ Представление постов пользователя
    """
    user_posts = posts_dao.get_by_user(username)
    bookmarks = posts_dao.get_bookmarks_all()
    return render_template('user-feed.html', posts=user_posts, bookmarks=bookmarks)

@main_blueprint.route('/bookmarks/add/<int:postid>')
def add_mark_page(postid):
    """ Представление добавления поста в закладки
    """
    post = posts_dao.get_by_pk(postid)
    posts_dao.add_bookmarks(post)
    return redirect('/', code=302)


@main_blueprint.route('/bookmarks/remove/<int:postid>')
def remove_mark_page(postid):
    """ Представление удаления поста в закладки
    """
    post = posts_dao.get_by_pk(postid)
    posts_dao.remove_bookmarks(post)
    return redirect('/', code=302)

@main_blueprint.route('/bookmarks/')
def bookmarks_page():
    """ Представление удаления поста в закладки
    """
    bookmarks_posts = posts_dao.get_bookmarks_all()
    return render_template('bookmarks.html', posts=bookmarks_posts)
