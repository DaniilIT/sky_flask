import pytest


class TestApi:
    def test_api_posts(self, test_client, post_key_should_be):
        """ Проверяем представление списка постов
        """
        response = test_client.get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, 'Статус код не верный'
        posts = response.json
        assert isinstance(posts, list), 'Возвращается не список'
        assert len(posts) > 0, 'Возвращается пустой список'
        assert set(posts[0].keys()) == post_key_should_be, 'неверный словарь в списке'

    def test_api_post_by_id(self, test_client, post_key_should_be):
        """ Проверяем представление поста по идентификатору
        """
        response = test_client.get('/api/posts/1')
        assert response.status_code == 200, 'Статус код не верный'
        post = response.json
        assert isinstance(post, dict), 'Возвращается не словарь'
        assert set(post.keys()) == post_key_should_be, 'неверный словарь'
