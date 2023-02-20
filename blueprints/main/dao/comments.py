import json
# from blueprints.main.dao.comment import Comment


COMMENTS_JSON_PATH = './data/comments.json'


class Comment:
    def __init__(self, post_id: int, commenter_name: str, comment: str, pk: int):
        self.post_id = post_id  # к какому посту этот комментарий
        self.commenter_name = commenter_name  # имя комментатора
        self.comment = comment  # текст комментария
        self.pk = pk  # id комментария

    def __repr__(self):
        return f'pk: {self.pk}'


class CommentsDAO:
    @staticmethod
    def get_all() -> list[Comment]:
        """ Возвращает все посты
        """
        comments = []

        with open(COMMENTS_JSON_PATH, 'r', encoding='utf-8') as json_file:
            raw_comments = json.load(json_file)

            for comment in raw_comments:
                comments.append(
                    Comment(comment.get('post_id'), comment.get('commenter_name'), comment.get('comment'), comment.get('pk'))
                )

        return comments
