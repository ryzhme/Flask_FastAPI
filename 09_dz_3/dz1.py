"""
Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль"
и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных,
а пароль должен быть зашифрован.
"""

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
from form_dz import RegistrationForm
from models_dz import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = b'79a3ff5a53fcd8cdf8418bd7e1df159453604516f47bdbdf0d9966dccd0574c6'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)


def add_user_to_db(firstname, lastname, email, password):
    new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()


def check_user_email_exists(email):
    exists_user = User.query.filter(User.email == email).all()
    if len(exists_user) > 0:
        return True
    return False


@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        hash_pwd = generate_password_hash(form.password.data)
        if check_user_email_exists(email):
            form.email.errors.append('Пользователь c таким email уже существует')
        else:
            add_user_to_db(firstname, lastname, email, hash_pwd)
            context = {'title': 'Успешная регистрация'}
            return render_template('success.html', **context)

    context = {'title': 'Регистрация'}
    return render_template('reg.html', **context, form=form)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run()
