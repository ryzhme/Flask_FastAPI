"""
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def text():
    return render_template('index5.html')


if __name__ == '__main__':
    app.run()
