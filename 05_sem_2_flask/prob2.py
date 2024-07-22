"""
Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
from pathlib import PurePath, Path
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/pict/')
def pict():
    return render_template('pict.html')


@app.route('/upload_pict/', methods=['GET', 'POST'])
def upload_pict():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = 'pict.jpg'
        file.save(PurePath.joinpath(Path.cwd(), 'static', file_name))
        return redirect(url_for('pict'))
    return render_template('upload_pict.html')


if __name__ == '__main__':
    app.run()
