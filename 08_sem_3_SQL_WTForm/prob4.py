"""
Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
○ Имя пользователя (обязательное поле)
○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке.
"""
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from form4 import RegistrationForm
from models4 import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = b'79a3ff5a53fcd8cdf8418bd7e1df159453604516f47bdbdf0d9966dccd0574c6'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


def add_user_to_db(name, email, password):
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()


def check_user_name_exists(name):
    exists_user = User.query.filter(User.name == name).all()
    if len(exists_user) > 0:
        return True
    return False


def check_user_email_exists(email):
    exists_user = User.query.filter(User.email == email).all()
    if len(exists_user) > 0:
        return True
    return False


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data
        email = form.email.data
        password = form.password.data
        if check_user_name_exists(name):
            form.name.errors.append('Пользователь уже существует')
        elif check_user_email_exists(email):
            form.email.errors.append('Пользователь c таким email уже существует')
        else:
            add_user_to_db(name, email, password)
            return '<h1>Вы успешно зарегистрированы=)</h1>'

    return render_template('register.html', form=form)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run()
