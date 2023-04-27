from dao import Comment


class TestBookmarksDAO:
    def test_get_all(self, comments_dao):
        """ Проверяем возврат всех комментариев
        """
        comments = comments_dao.get_all()
        assert isinstance(comments, list)
        assert len(comments) > 0
        assert isinstance(comments[0], Comment)
