import json


def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict]:
    res = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            res.append(post)
    return res
