import json
# from blueprints.main.dao.post import Post
from blueprints.main.dao.comments import CommentsDAO


POSTS_JSON_PATH = './data/posts.json'


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

    @staticmethod
    def get_post_dict(post) -> dict:
        """ Возвращает пост в виде словаря
        """
        return {
            'poster_name': post.poster_name,
            'poster_avatar': post.poster_avatar,
            'pic': post.pic,
            'content': post.content,
            'views_count': post.views_count,
            'likes_count': post.likes_count,
            'pk': post.pk,
        }

    def __repr__(self):
        return f'pk: {self.pk}'


class PostsDAO:
    @staticmethod
    def get_all() -> list[Post]:
        """ Возвращает все посты
        """
        posts = []

        with open(POSTS_JSON_PATH, 'r', encoding='utf-8') as json_file:
            raw_posts = json.load(json_file)

            for post in raw_posts:
                posts.append(
                    Post(
                        post.get('poster_name'), post.get('poster_avatar'), post.get('pic'), post.get('content'),
                        post.get('views_count'), post.get('likes_count'), post.get('pk')
                    )
                )

        return posts

    def get_by_pk(self, pk: int) -> Post:
        """ Возвращает пост по его идентификатору
        """
        posts = self.get_all()

        for post in posts:
            if post.pk == pk:
                return post

        raise ValueError('post with this id does not exist')

    def get_by_user(self, user_name: str) -> list[Post]:
        """ Возвращает список постов пользователя
        """
        posts = self.get_all()

        user_posts = []
        for post in posts:
            if post.poster_name == user_name:
                user_posts.append(post)

        if len(user_posts) == 0:
            raise ValueError('user with this name does not exist')

        return user_posts

    def get_comments_by_post_id(self, post_id: int) -> list:
        """ Возвращает комментарии к посту
        """
        posts = self.get_all()

        post_keys = {post.pk for post in posts}
        if post_id not in post_keys:
            raise ValueError('post with this id does not exist')

        comments = CommentsDAO.get_all()

        post_comments = []
        for comment in comments:
            if comment.post_id == post_id:
                post_comments.append(comment)

        return post_comments

    def search(self, query: str) -> list[Post]:
        """ Возвращает список постов по ключевому слову
        """
        query_lower = query.lower()
        posts = self.get_all()

        query_posts = []
        for post in posts:
            if query_lower in post.content.lower():
                query_posts.append(post)

        return query_posts
