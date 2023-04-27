import json
from re import findall
from sys import getsizeof as gs

from flask import abort

from config import POSTS_JSON_PATH
from .post import Post
from .comments_dao import CommentsDAO


class PostsDAO:
    def __init__(self, json_path: str = POSTS_JSON_PATH):
        self.json_path = json_path
        self.posts = []

    def _load_json(self) -> list[Post]:
        """ Загрузка json DB
        """
        self.posts = []

        try:
            with open(self.json_path, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except (FileExistsError, json.JSONDecodeError):
            return abort(400)

    def load_database(self):
        for post in self._load_json():
            self.posts.append(
                Post(post.get('poster_name'), post.get('poster_avatar'), post.get('pic'), post.get('content'),
                     post.get('views_count'), post.get('likes_count'), post.get('pk'))
            )

    def upload(self, post):
        """ Запись в json DB
        """
        database = self._load_json()
        database.append(post)

        with open(self.json_path, 'w') as json_file:
            json.dump(database, json_file, indent=2, ensure_ascii=False)

    def get_all(self) -> list[Post]:
        return self.posts

    def get_by_pk(self, pk: int) -> Post:
        """ Возвращает пост по его идентификатору
        """
        for post in self.posts:
            if post.pk == pk:
                return post
        else:
            abort(404)

    def get_by_user(self, user_name: str) -> list[Post]:
        """ Возвращает список постов пользователя
        """
        user_posts = []
        for post in self.posts:
            if post.poster_name == user_name:
                user_posts.append(post)

        return user_posts

    def search(self, query: str) -> list[Post]:
        """ Поиск постов по ключевому слову
        """
        # query_lower = query.lower()

        query_posts = []
        for post in self.posts:
            if query.lower().strip() in findall(r'\w+', post.content.lower()):
                query_posts.append(post)
            # if query_lower in post.content.lower():
            #     query_posts.append(post)

        return query_posts

    def get_comments_by_post_id(self, post_id: int, comments_dao: CommentsDAO) -> list:
        """ Возвращает комментарии к посту
        """

        post_keys = {post.pk for post in self.posts}
        if post_id not in post_keys:
            raise ValueError('post with this id does not exist')

        comments = comments_dao.get_all()

        post_comments = []
        for comment in comments:
            if comment.post_id == post_id:
                post_comments.append(comment)

        return post_comments

    def __repr__(self):
        """ Информация о размере DB
        """
        return f'DB: {self.path}\nСодержит записей: {len(self.posts)}\nРазмер DB: {gs(PostsDAO)} Байт.'
