from flask import Blueprint, render_template
from utils import get_posts_all


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def index_page():
    posts = get_posts_all()
    for post in posts:
        post['content'] = f'{post["content"][:24]}...'
    return render_template('index.html', posts=posts)
