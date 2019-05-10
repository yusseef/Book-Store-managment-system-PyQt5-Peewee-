from peewee import *
import datetime
db = SqliteDatabase('library.db')


class Client(Model):
    #name,phone number, age, email, join date.
    Name = TextField(unique=True, null=False)
    PhoneNumber = IntegerField(default=0, null=False)
    Age = DecimalField(default=0)
    email = CharField(unique=True, null=False)
    added = TextField()

    class Meta:
        database = db


class Users(Model):
    #name,phone number, email, password.
    Name = TextField()
    PhoneNumber = IntegerField()
    email = CharField()
    Password = CharField()
    Salary = DecimalField()
    Job_title = TextField()
    today_permission = CharField()
    books_permission = CharField()
    client_permission = CharField()
    setting_permission = CharField()


    class Meta:

        database = db


class Books(Model):

   #book name, price, book description

    Book_name = TextField( unique=True, null=False)
    Price = DecimalField(default=0, null=False)
    Book_description = CharField(max_length=255)
    qty = DecimalField(default=0, null=False)
    added = TextField()


    class Meta:
        database = db


class today(Model):
    #
    book_title = TextField( null=False)
    qty = IntegerField(default=0, null=False)
    price = DecimalField(default=0, null=False)
    name = TextField( null=False)

    class Meta:
        database = db



class loan_bonus(Model):
    User_name = TextField()
    loan = DecimalField()
    bonus = DecimalField()
    final_salary = DecimalField()

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    db.create_tables([Client, Users, Books, today,loan_bonus])


