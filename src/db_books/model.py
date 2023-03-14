from peewee import *

db = SqliteDatabase('./src/db_books/books.db')

class Books(Model):
    title = CharField(40)
    authors = CharField(60)
    categories = CharField(100)
    thumbnail = CharField(100)
    description = CharField(400)
    published_year = IntegerField()
    average_rating = FloatField()
    num_pages = IntegerField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'

if __name__ == '__main__':
    Books.create_table()