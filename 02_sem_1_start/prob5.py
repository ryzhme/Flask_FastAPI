"""
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""

from flask import Flask

app = Flask(__name__)

html = """
<html>
<head>
    <meta charset="utf-8">
    <title>Моя первая HTML страница</title>
</head>
<body>
    <p>Привет, мир!</p>
</body>
</html>
"""


@app.route('/')
def text():
    return html


if __name__ == '__main__':
    app.run()
