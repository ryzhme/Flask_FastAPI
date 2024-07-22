"""
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.get('/submit/')
def submit_get():
    return render_template('form.html')


@app.post('/submit/')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run()
