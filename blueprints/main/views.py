from logger_init import logger_mine
from flask import Blueprint, render_template, request, redirect
import config
from dao import PostsDAO
from dao import CommentsDAO
from dao import BookmarksDAO


main_blueprint = Blueprint('main', __name__, template_folder='templates')

posts_dao = PostsDAO(config.POSTS_JSON_PATH)
comments_dao = CommentsDAO(config.COMMENTS_JSON_PATH)
bookmarks_dao = BookmarksDAO(config.BOOKMARKS_JSON_PATH)


@main_blueprint.route('/')
def main_page():
    """ Представление основной страницы
    """
    # обновляем загрузку DB
    posts_dao.load_database()
    return render_template('index.html')


@main_blueprint.route('/posts/<int:post_id>')
def post_by_id_page(post_id):
    """ Представление поста по идентификатору
    """
    post = posts_dao.get_by_pk(post_id)
    comments = posts_dao.get_comments_by_post_id(post_id, comments_dao)
    bookmarks = bookmarks_dao.get_all()
    return render_template('post.html', post=post, comments=comments, bookmarks=bookmarks)


@main_blueprint.route('/all/')
def index_page():
    """ Представление ленты постов
    """
    posts = posts_dao.get_all()
    bookmarks = bookmarks_dao.get_all()
    return render_template('all.html', posts=posts, bookmarks=bookmarks)


@main_blueprint.route('/search/')  # , methods=['GET'])
def search_page():
    """ Представление поиска постов по ключевому слову.
    """
    if search_request := request.args.get('s'):
        filtered_database = posts_dao.search(search_request)[:10]
    else:
        return redirect('/all/', code=302)

    logger_mine.info(f'Search request: {search_request}')

    return render_template(
        'post_list.html',
        search_request=search_request,
        filtered_database=filtered_database
    )


# @main_blueprint.route('/search/', methods=['GET'])
# def search_page():
#     """ Представление поиска постов по ключевому слову
#     """
#     s = request.args.get('s')
#     query_posts = posts_dao.search(s)[:10]
#     bookmarks = bookmarks_dao.get_all()
#     return render_template('search.html', posts=query_posts, bookmarks=bookmarks)


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
