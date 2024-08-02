from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'Author({self.firstname}, {self.lastname})'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    cnt = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'Book({self.name}, {self.year})'
