from dao.post import Post


class TestBookmarksDAO:
    def test_get_all(self, bookmarks_dao):
        """ Проверяем возврат всех постов
        """
        posts = bookmarks_dao.get_all()
        assert isinstance(posts, list)
        if len(posts) > 0:
            assert isinstance(posts[0], Post)
