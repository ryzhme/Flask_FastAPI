"""
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def main():
    context = {'title': 'Магазин'}
    return render_template('index.html', **context)


@app.route('/cloth/')
def cloth():
    _cloth = [{
            'title': 'Куртка',
            'brand': 'ИП Семенов',
            'prise': '13',
            'id':    '999'
        },
        {
            'title': 'Кофта',
            'brand': 'Zara',
            'prise': '25'
        },
        {
            'title': 'Брюки',
            'brand': 'Henderson',
            'prise': '30'
        },
    ]
    context = {'title': 'Одежда', 'cloth': _cloth}
    return render_template('cloth.html', **context)


@app.route('/shoes/')
def shoes():
    _shoes = [{
            'title': 'Кросовки',
            'brand': 'Adidas',
            'prise': '250'
        },
        {
            'title': 'Туфли',
            'brand': 'VALENTINO GARAVANI',
            'prise': '700'
        },
        {
            'title': 'Лоферы',
            'brand': 'LORO PIANA',
            'prise': '1000'
        },
    ]
    context = {'title': 'Обувь', 'shoes': _shoes}
    return render_template('shoes.html', **context)


@app.route('/item/<int:item_id>')
def item(item_id):
    # этот item подгрузился из базы по id
    item = {'title': 'Куртка',
            'brand': 'ИП Семенов',
            'prise': '13',
            'id':    '999'}
    context = {'title': 'Товар', 'item_id': item_id, 'item': item}
    return render_template('item.html', **context)


if __name__ == '__main__':
    app.run()
