class Post:
    def __init__(self, poster_name: str, poster_avatar: str, pic: str, content: str,
                 views_count: int, likes_count: int, pk: int):
        self.poster_name = poster_name  # имя автора поста
        self.poster_avatar = poster_avatar  # аватарка автора поста
        self.pic = pic  # картинка поста
        self.content = content  # текст поста
        self.views_count = views_count  # количество просмотров
        self.likes_count = likes_count  # количество лайков
        self.pk = pk  # id поста

    def get_post_dict(self) -> dict:
        """ Возвращает пост в виде словаря
        """
        return {
            'poster_name': self.poster_name,
            'poster_avatar': self.poster_avatar,
            'pic': self.pic,
            'content': self.content,
            'views_count': self.views_count,
            'likes_count': self.likes_count,
            'pk': self.pk,
        }

    def __eq__(self, other_post):
        return self.pk == other_post.pk

    def __repr__(self):
        return f'№{self.pk}'
