from Bank import bank


class users(object):

    def __init__(self, id_user=0, name="", name_mom="", CPF_mom="", CPF="", RG="", SUS_card="", sex="", phone="",
                 email="", password="", city="", district="", road="", number="", complement="", day="", month="",
                 year=""):
        self.info = {}
        self.id_user = id_user
        self.name = name
        self.name_mom = name_mom
        self.CPF_mom = CPF_mom
        self.CPF = CPF
        self.RG = RG
        self.SUS_card = SUS_card
        self.sex = sex
        self.phone = phone
        self.email = email
        self.password = password
        self.city = city
        self.district = district
        self.road = road
        self.number = number
        self.complement = complement
        self.day = day
        self.month = month
        self.year = year

    def create_user(self, ID=None):
        database = bank()

        try:
            c = database.user_connection.cursor()

            c.execute("insert into users (name, name_mom, CPF_mom, CPF, RG, SUS_card, sex, phone, email, password) "
                      "values ('" + self.name + "', '" + self.name_mom + "', '" + self.CPF_mom + "', '" + self.CPF
                      + "', '" + self.RG + "', '" + self.SUS_card + "', '" + self.sex + "', '" + self.phone + "', '" +
                      self.email + "', '" + self.password + "' )")

            database.user_connection.commit()
            c.close()

            c = database.address_connection.cursor()

            c.execute("insert into address (city, district, road, number, complement) values ('" +
                      self.city + "', '" + self.district + "', '" + self.road + "', '" +
                      self.number + "', '" + self.complement + "' )")

            database.address_connection.commit()
            c.close()

            c = database.birthday_connection.cursor()

            c.execute("insert into birthday (day, month, year) values ('" +
                      self.day + "', '" + self.month + "', '" + self.year + "' )")

            database.birthday_connection.commit()
            c.close()

            c = database.user_connection.cursor()

            c.execute("select id_user from users "
                      "where password=?"
                      "and name=?"
                      "and CPF=?", (self.password, self.name, self.CPF))

            for line in c:
                ID = str(line[0])

            c.close()

            return "Usuário cadastrado com sucesso! seu id é " + ID + " "
        except:
            return "Ocorreu um erro na inserção do usuário"

    def selectUser(self, id_user, password):
        database = bank()

        try:

            c = database.user_connection.cursor()

            c.execute("select password from users where id_user = " + id_user + " ")

            for psswrd in c:
                if password == psswrd[0]:
                    c.close()
                    return True

            c.close()

        except:
            return False

    def search_id(self, ID=None):
        database = bank()

        try:
            c = database.user_connection.cursor()

            c.execute("select id_user from users "
                      "where password=?"
                      "and name=?"
                      "and CPF=?", (self.password, self.name, self.CPF))

            for line in c:
                ID = str(line[0])

            c.close()
            return "Seu id é " + ID + " "

        except:
            return "id não encontrado"
