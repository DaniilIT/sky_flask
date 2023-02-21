import json


class Comment:
    def __init__(self, post_id: int, commenter_name: str, comment: str, pk: int):
        self.post_id = post_id  # к какому посту этот комментарий
        self.commenter_name = commenter_name  # имя комментатора
        self.comment = comment  # текст комментария
        self.pk = pk  # id комментария

    def __repr__(self):
        return f'№{self.pk}'


class CommentsDAO:
    def __init__(self, json_path: str):
        self.json_path = json_path

    def get_all(self) -> list[Comment]:
        """ Возвращает все посты
        """
        comments = []

        with open(self.json_path, 'r', encoding='utf-8') as json_file:
            raw_comments = json.load(json_file)

            for comment in raw_comments:
                comments.append(
                    Comment(comment.get('post_id'), comment.get('commenter_name'), comment.get('comment'),
                            comment.get('pk'))
                )

        return comments
