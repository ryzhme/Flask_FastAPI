"""
Создать базу данных для хранения информации о студентах университета.
    База данных должна содержать две таблицы: "Студенты" и "Факультеты".
    В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
    возраст, пол, группа и id факультета.
    В таблице "Факультеты" должны быть следующие поля: id и название
    факультета.
    Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
"""
from flask import Flask, render_template, jsonify
from models1 import db, Faculty, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_db.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/students/')
def students():
    students = db.session.query(Student, Faculty).join(Faculty, Faculty.id == Student.faculty_id).all()
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run()
