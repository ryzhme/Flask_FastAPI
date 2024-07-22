"""
Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""
from pathlib import PurePath, Path
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['login'] == 'max' and request.form['password'] == 'max':
            return redirect(url_for('greetings'))
        else:
            return redirect(url_for('login_err'))
    return render_template('login.html')


@app.route('/login_err/')
def login_err():
    return render_template('login_err.html')


@app.route('/greetings/')
def greetings():
    return render_template('greetings.html')


if __name__ == '__main__':
    app.run()
