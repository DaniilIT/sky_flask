import json
from .post import Post


class BookmarksDAO:
    def __init__(self, json_path: str):
        self.json_path = json_path

    def get_all(self) -> list[Post]:
        """ Возвращает все закладки
        """
        bookmarks = []

        with open(self.json_path, 'r', encoding='utf-8') as json_file:
            raw_posts = json.load(json_file)

            for post in raw_posts:
                bookmarks.append(
                    Post(
                        post.get('poster_name'), post.get('poster_avatar'), post.get('pic'), post.get('content'),
                        post.get('views_count'), post.get('likes_count'), post.get('pk')
                    )
                )

        return bookmarks

    def write_all(self, bookmarks):
        """ Записывает закладки
        """
        raw_posts = []
        for post in bookmarks:
            raw_posts.append(post.get_post_dict())

        with open(self.json_path, 'w') as json_file:
            json.dump(raw_posts, json_file, indent=2, ensure_ascii=False)

    def add_bookmark(self, post: Post):
        """ Добавить пост в закладку
        """
        bookmarks = self.get_all()

        if post not in bookmarks:
            bookmarks.append(post)
            self.write_all(bookmarks)

    def remove_bookmark(self, post: Post):
        """ Удалить пост из закладок
        """
        bookmarks = self.get_all()

        if post in bookmarks:
            bookmarks.remove(post)
            self.write_all(bookmarks)
