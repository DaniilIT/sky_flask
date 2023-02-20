import pytest
from app import app

@pytest.fixture()
def test_client():
    return app.test_client()

@pytest.fixture()
def post_key_should_be():
    return {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

@pytest.fixture()
def comments_key_should_be():
    return {'post_id', 'commenter_name', 'comment', 'pk'}
