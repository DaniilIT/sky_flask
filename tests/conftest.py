import pytest
import config
from app import app
from blueprints.main.dao.posts_dao import PostsDAO
from blueprints.main.dao.comments_dao import CommentsDAO
from blueprints.main.dao.bookmarks_dao import BookmarksDAO


@pytest.fixture()
def test_client():
    return app.test_client()


@pytest.fixture()
def post_key_should_be():
    return {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


@pytest.fixture()
def comments_key_should_be():
    return {'post_id', 'commenter_name', 'comment', 'pk'}


@pytest.fixture()
def posts_dao():
    return PostsDAO(config.POSTS_JSON_PATH)


@pytest.fixture()
def comments_dao():
    return CommentsDAO(config.COMMENTS_JSON_PATH)


@pytest.fixture()
def bookmarks_dao():
    return BookmarksDAO(config.BOOKMARKS_JSON_PATH)
