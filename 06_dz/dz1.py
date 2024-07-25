'''
Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл
с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
'''

from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/greetings/')
def greetings():
    context = {'username': request.cookies.get('username')}
    return render_template('greetings.html', **context)


@app.route('/exit/')
def exit():
    response = make_response(redirect(url_for('form')))
    response.set_cookie('username', '0', max_age=0)
    response.set_cookie('email', '0', max_age=0)
    return response


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        response = make_response(redirect(url_for('greetings')))
        response.set_cookie('username', request.form['username'])
        response.set_cookie('email', request.form['email'])
        return response
    return render_template('form.html')


if __name__ == '__main__':
    app.run()
