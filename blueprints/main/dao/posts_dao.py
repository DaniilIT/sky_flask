import json
from .post import Post
from .comments_dao import CommentsDAO


class PostsDAO:
    def __init__(self, json_path: str):
        self.json_path = json_path

    def get_all(self) -> list[Post]:
        """ Возвращает все посты
        """
        posts = []

        with open(self.json_path, 'r', encoding='utf-8') as json_file:
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

    def get_comments_by_post_id(self, post_id: int, comments_dao: CommentsDAO) -> list:
        """ Возвращает комментарии к посту
        """
        posts = self.get_all()

        post_keys = {post.pk for post in posts}
        if post_id not in post_keys:
            raise ValueError('post with this id does not exist')

        comments = comments_dao.get_all()

        post_comments = []
        for comment in comments:
            if comment.post_id == post_id:
                post_comments.append(comment)

        return post_comments
