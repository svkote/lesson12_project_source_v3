import json


def load_posts() -> list[dict]:
    """Загружает посты"""
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_word(word: str) -> list[dict]:
    """Возвращает посты по ключевому слову"""
    res = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            res.append(post)
    return res


def add_post(post: dict) -> dict:
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f)
    return post


def save_picture(picture) -> str:
    filename = picture.filename
    pic_path = f'./uploads/images/{filename}'
    picture.save(pic_path)
    return pic_path
