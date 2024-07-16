"""
Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/about/')
def about():
    context = {'title': 'О нас'}
    return render_template('about8.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты'}
    return render_template('contacts8.html', **context)


if __name__ == '__main__':
    app.run()
