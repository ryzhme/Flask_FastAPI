from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_4 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'79a3ff5a53fcd8cdf8418bd7e1df159453604516f47bdbdf0d9966dccd0574c6'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
