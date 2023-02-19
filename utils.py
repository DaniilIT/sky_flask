import json


POSTS_JSON_PATH = './data/posts.json'
COMMENTS_JSON_PATH = './data/comments.json'


def get_posts_all() -> list:
    """ Возвращает все посты
    """
    posts = []
    with open(POSTS_JSON_PATH, 'r', encoding='utf-8') as json_file:
        posts = json.load(json_file)
    return posts


def get_posts_by_user(user_name: str) -> list:
    """ Возвращает список постов пользователя
    """
    posts = get_posts_all()

    user_posts = []
    for post in posts:
        if post.get('poster_name') == user_name:
            user_posts.append(post)

    if len(user_posts) == 0:
        raise ValueError(f'user with this name does not exist')

    return user_posts


def get_comments_by_post_id(post_id: int) -> list:
    """ Возвращает комментарии к посту
    """
    posts = get_posts_all()

    post_keys = {post.get('pk') for post in posts}
    if post_id not in post_keys:
        raise ValueError(f'post with this id does not exist')

    comments = []
    with open(COMMENTS_JSON_PATH, 'r', encoding='utf-8') as json_file:
        comments = json.load(json_file)

    post_comments = []
    for comment in comments:
        if comment.get('post_id') == post_id:
            post_comments.append(comment)

    return post_comments


def search_for_posts(query: str) -> list:
    """ Возвращает список постов по ключевому слову
    """
    query_lower = query.lower()
    posts = get_posts_all()

    query_posts = []
    for post in posts:
        if query_lower in post.get('content').lower():
            query_posts.append(post)

    return query_posts


def get_posts_by_pk(pk: int) -> dict:
    """ Возвращает пост по его идентификатору
    """
    posts = get_posts_all()

    for post in posts:
        if post.get('pk') == pk:
            return post

    raise ValueError(f'post with this id does not exist')
