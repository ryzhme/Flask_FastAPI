"""
Задание №2
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.
"""

from flask import Flask, render_template
from models2 import db, Author, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/books/')
def books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)


if __name__ == '__main__':
    app.run()
