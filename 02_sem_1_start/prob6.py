"""
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def text():
    _students = [{
            'firstname': 'Иванов',
            'lastname': 'Семен',
            'age': '18',
            'rating': '3.8'
        },
        {
            'firstname': 'Кузнецов',
            'lastname': 'Филипп',
            'age': '19',
            'rating': '4.3'
        },
        {
            'firstname': 'Шапка',
            'lastname': 'Егор',
            'age': '20',
            'rating': '3.3'
        },
        {
            'firstname': 'Романова',
            'lastname': 'Наталья',
            'age': '21',
            'rating': '4.99'
        }, ]
    context = {'students': _students}
    return render_template('index6.html', **context)


if __name__ == '__main__':
    app.run()