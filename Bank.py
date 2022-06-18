import sqlite3


class bank:
    def __init__(self):
        self.user_connection = sqlite3.connect('bank.db')
        self.address_connection = sqlite3.connect('bank.db')
        self.birthday_connection = sqlite3.connect('bank.db')

        self.createTable()

    def createTable(self):
        c = self.user_connection.cursor()

        c.execute("""create table if not exists users (
                     id_user integer primary key autoincrement ,
                     name text,
                     name_mom text,
                     CPF_mom text,
                     CPF text,
                     RG text,
                     SUS_card text,
                     sex text,
                     phone text,
                     email text,
                     password text)""")

        self.user_connection.commit()
        c.close()

        c = self.address_connection.cursor()

        c.execute("""create table if not exists address (
                    id_user integer primary key autoincrement ,
                    city text,
                    district text,
                    road text,
                    number text,
                    complement text)""")

        self.address_connection.commit()
        c.close()

        c = self.birthday_connection.cursor()

        c.execute("""create table if not exists birthday (
                    id_user integer primary key autoincrement ,
                    day integer,
                    month integer,
                    year integer)""")

        self.birthday_connection.cursor()
        c.close()
