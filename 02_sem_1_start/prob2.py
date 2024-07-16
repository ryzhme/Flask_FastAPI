"""
Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше вебприложение:
○ страницу "about"
○ страницу "contact".
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World 11'


@app.route('/about/')
def about():
    return 'всякий абаут здесь написан'


@app.route('/contact/')
def contact():
    return 'Есть контакт!'


if __name__ == '__main__':
    app.run()
