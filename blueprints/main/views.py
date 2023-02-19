from flask import Blueprint, render_template
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
