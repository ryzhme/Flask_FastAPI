"""
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/text/', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        word_list = request.form['text'].split()
        print(word_list)
        return f'количество слов: {len(word_list)}'
    return render_template('text_form.html')


if __name__ == '__main__':
    app.run()
