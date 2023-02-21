import pytest


class TestMain:
    def test_main_index(self, test_client):
        response = test_client.get('/')
        assert response.status_code == 200

    def test_main_post_by_id(self, test_client):
        response = test_client.get('/posts/1', follow_redirects=True)
        assert response.status_code == 200

    def test_main_search(self, test_client):
        params = {'s': 'кот'}
        response = test_client.get('/posts/1', query_string=params, follow_redirects=True)
        assert response.status_code == 200

    def test_main_users(self, test_client):
        response = test_client.get('/users/leo', follow_redirects=True)
        assert response.status_code == 200

    def test_main_add_mark(self, test_client):
        response = test_client.get('/bookmarks/add/1', follow_redirects=False)
        assert response.status_code == 302

    def test_main_remove_mark(self, test_client):
        response = test_client.get('/bookmarks/remove/1', follow_redirects=False)
        assert response.status_code == 302
