"""
Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/<string>/')
def get_len(string):
    return f'{len(string)}'


if __name__ == '__main__':
    app.run()
