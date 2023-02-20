from flask import Blueprint, render_template, request
from utils import *


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def index_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:postid>')
def posts_page(postid):
    post = get_posts_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search/', methods=['GET'])
def search_page():
    s = request.args.get('s')
    query_posts = search_for_posts(s)[:10]
    return render_template('search.html', posts=query_posts)
