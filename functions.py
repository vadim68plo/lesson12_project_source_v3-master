import json

from config import DATA

def load_posts_from_json(path=DATA):

    '''Возвращает список всех постов'''

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except:
        print("Файл не найден")


def search_post(post_in):

    '''Возвращает список всех постов по введеному слову'''

    posts = load_posts_from_json()
    _search_post = []
    for post in posts:
        if post_in.lower() in post["content"].lower():
            _search_post.append(post)

    if len(_search_post) == 0:
        return "Пост не найден"
    else:
        return _search_post


def load_post(name, post):

    '''Загружает файлы в json файл'''

    posts = load_posts_from_json()
    load_data = {"pic": name, "content": post}
    posts.append(load_data)

    with open("posts.json", "w", encoding="utf-8") as outfile:
        json.dump(posts, outfile, ensure_ascii=False, indent=2)



















