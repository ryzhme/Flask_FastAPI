from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = b'79a3ff5a53fcd8cdf8418bd7e1df159453604516f47bdbdf0d9966dccd0574c6'
csrf = CSRFProtect(app)

"""
в терминале ввести python
import secrets
secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protaction!'


if __name__ == '__main__':
    app.run()
