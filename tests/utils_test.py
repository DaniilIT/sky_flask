import pytest
from utils import *

POST_KEY_SHOULD_BE = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
COMMENTS_KEY_SHOULD_BE = {'post_id', 'commenter_name', 'comment', 'pk'}


class TestGetPostsAll:
    def test_get_posts_all(self):
        """ Проверяем возврат всех постов
        """
        posts = get_posts_all()
        assert type(posts) == list, 'возвращается не список'
        assert len(posts) > 0, 'возвращается пустой список'
        assert set(posts[0].keys()) == POST_KEY_SHOULD_BE, 'неверный список'


class TestGetPostsByUser:
    def test_get_posts_by_user(self):
        """ Проверяем возврат списка постов пользователя
        """
        user_name = 'leo'
        user_posts = get_posts_by_user(user_name)
        assert type(user_posts) == list, 'возвращается не список'
        assert len(user_posts) == 2, 'возвращается список не той длины'
        assert set(user_posts[0].keys()) == POST_KEY_SHOULD_BE, 'неверный список'

    def test_value_error_get_posts_by_user(self):
        """ Проверяем возврат списка постов несуществующего пользователя
        """
        with pytest.raises(ValueError):
            user_name = 'not exist'
            user_posts = get_posts_by_user(user_name)


class TestGetCommentsByPostId:
    def test_get_comments_by_post_id(self):
        """ Проверяем возврат комментариев к посту
        """
        post_id = 1
        post_comments = get_comments_by_post_id(post_id)
        assert type(post_comments) == list, 'возвращается не список'
        assert len(post_comments) == 4, 'возвращается список не той длины'
        assert set(post_comments[0].keys()) == COMMENTS_KEY_SHOULD_BE, 'неверный список'

    def test_get_comments_by_post_id_empty(self):
        """ Проверяем возврат комментариев к посту, к которому нет комментариев
        """
        post_id = 8
        post_comments = get_comments_by_post_id(post_id)
        assert type(post_comments) == list, 'возвращается не список'
        assert len(post_comments) == 0, 'возвращается список не той длины'

    def test_value_error_get_comments_by_post_id(self):
        """ Проверяем возврат комментариев к несуществующему посту
        """
        with pytest.raises(ValueError):
            post_id = 9
            post_comments = get_comments_by_post_id(post_id)


class TestSearchForPosts:
    def test_search_for_posts(self):
        """ Проверяем возврат списка постов по ключевому слову
        """
        query = 'очень'
        query_posts = search_for_posts(query)
        assert type(query_posts) == list, 'возвращается не список'
        assert len(query_posts) > 0, 'возвращается пустой список'
        assert set(query_posts[0].keys()) == POST_KEY_SHOULD_BE, 'неверный список'



class TestGetPostsByPk:
    """ Проверяем возврат поста по его идентификатору
    """
    def test_get_posts_by_pk(self):
        pk = 1
        post = get_posts_by_pk(pk)
        assert type(post) == dict, 'возвращается не словарь'
        assert set(post.keys()) == POST_KEY_SHOULD_BE, 'неверный словарь'
        assert post.get('poster_name') == 'leo', 'не тот словарь'

    def test_value_error_get_posts_by_pk(self):
        """ Проверяем возврат несуществующего поста
        """
        with pytest.raises(ValueError):
            pk = 9
            post = get_posts_by_pk(pk)
