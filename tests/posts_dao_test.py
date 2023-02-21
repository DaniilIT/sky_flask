import pytest
from blueprints.main.dao.post import Post
from blueprints.main.dao.comments_dao import Comment


class TestPostsDAO:
    def test_get_all(self, posts_dao):
        """ Проверяем возврат всех постов
        """
        posts = posts_dao.get_all()
        assert isinstance(posts, list)
        assert len(posts) > 0
        assert isinstance(posts[0], Post)

    def test_get_by_pk(self, posts_dao):
        """ Проверяем возврат поста по его идентификатору
        """
        pk = 1
        post = posts_dao.get_by_pk(pk)
        assert isinstance(post, Post)
        assert post.pk == 1

    def test_value_error_get_by_pk(self, posts_dao):
        """ Проверяем возврат несуществующего поста
        """
        with pytest.raises(ValueError):
            posts_dao.get_by_pk(0)

    def test_get_by_user(self, posts_dao, post_key_should_be):
        """ Проверяем возврат списка постов пользователя
        """
        user_name = 'leo'
        user_posts = posts_dao.get_by_user(user_name)
        assert isinstance(user_posts, list)
        assert len(user_posts) > 0
        assert isinstance(user_posts[0], Post)

    def test_value_error_get_by_user(self, posts_dao):
        """ Проверяем возврат списка постов несуществующего пользователя
        """
        with pytest.raises(ValueError):
            posts_dao.get_by_user('not exist')

    def test_get_comments_by_post_id(self, posts_dao, comments_dao):
        """ Проверяем возврат комментариев к посту
        """
        post_id = 1
        post_comments = posts_dao.get_comments_by_post_id(post_id, comments_dao)
        assert isinstance(post_comments, list)
        assert len(post_comments) > 0
        assert isinstance(post_comments[0], Comment)

    def test_get_comments_by_post_id_empty(self, posts_dao, comments_dao):
        """ Проверяем возврат комментариев к посту, к которому нет комментариев
        """
        post_id = 8
        post_comments = posts_dao.get_comments_by_post_id(post_id, comments_dao)
        assert isinstance(post_comments, list)
        assert len(post_comments) == 0

    def test_value_error_get_comments_by_post_id(self, posts_dao, comments_dao):
        """ Проверяем возврат комментариев к несуществующему посту
        """
        with pytest.raises(ValueError):
            posts_dao.get_comments_by_post_id(9, comments_dao)

    def test_search(self, posts_dao, post_key_should_be):
        """ Проверяем возврат списка постов по ключевому слову
        """
        query = 'очень'
        query_posts = posts_dao.search(query)
        assert isinstance(query_posts, list)
        assert len(query_posts) > 0
        assert isinstance(query_posts[0], Post)
