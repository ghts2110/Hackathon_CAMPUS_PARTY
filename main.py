from tkinter import *
from User import users
from Profile import menu


class Application:
    def __init__(self, master=None):
        self.container4 = None
        self.sex = None
        self.container3 = None
        self.container2 = None
        self.container1 = None
        self.CPF_mom = None
        self.id_user = None
        self.id_user_container = None
        self.year = None
        self.month = None
        self.day = None
        self.birthday_container = None
        self.complement = None
        self.number = None
        self.road = None
        self.district = None
        self.city = None
        self.address1_container = None
        self.address2_container = None
        self.address3_container = None
        self.SUS_card = None
        self.RG = None
        self.CPF = None
        self.name_mom = None
        self.msg_check = None
        self.msg_confirm = None
        self.password_container = None
        self.btn_container = None
        self.msg_container = None
        self.email = None
        self.phone = None
        self.name = None
        self.password = None
        self.font_pattern = ("Arial", "12")

        self.widget = Frame(master)
        self.widget.pack()

        self.login = Button(self.widget, text="Login", width=5, command=self.open_login)
        self.login.pack(side=LEFT)

        self.create = Button(self.widget, text="Criar", width=5, command=self.open_create)
        self.create.pack(side=RIGHT)

    def open_login(self, master=None):
        self.login.pack_forget()
        self.create.pack_forget()

        self.msg_container = Frame(master)
        self.msg_container["pady"] = 10
        self.msg_container.pack()

        self.id_user_container = Frame(master)
        self.id_user_container["padx"] = 20
        self.id_user_container.pack()
        
        self.password_container = Frame(master)
        self.password_container["padx"] = 20
        self.password_container.pack()

        self.btn_container = Frame(master)
        self.btn_container["padx"] = 20
        self.btn_container["pady"] = 10
        self.btn_container.pack()

        self.msg_check = Frame(master)
        self.msg_check["pady"] = 10
        self.msg_check.pack()

        title = Label(self.msg_container, text="Dados do usuário", font=("Arial", "10", "bold"))
        title.pack()

        id_user_Label = Label(self.id_user_container, text="ID:", font=self.font_pattern, width=10)
        id_user_Label.pack(side=LEFT)
        self.id_user = Entry(self.id_user_container, width=25, font=self.font_pattern)
        self.id_user.pack(side=LEFT)

        password_Label = Label(self.password_container, text="Senha:", font=self.font_pattern, width=10)
        password_Label.pack(side=LEFT)
        self.password = Entry(self.password_container,  width=25, font=self.font_pattern, show="*")
        self.password.pack(side=LEFT)

        come_back_btn = Button(self.btn_container, text="Voltar", font=("Calibri", "12"), width=7)
        come_back_btn["command"] = self.come_back
        come_back_btn.pack(side=LEFT)

        log_into = Button(self.btn_container, text="Logar", font=("Calibri", "12"), width=7)
        log_into["command"] = self.log_confirm
        log_into.pack(side=LEFT)

        id_info = Button(self.btn_container, text="Procurar id", font=("Calibri", "12"), width=7)
        id_info["command"] = self.search_id
        id_info.pack(side=LEFT)

        self.msg_confirm = Label(self.msg_check, text="", font=self.font_pattern)
        self.msg_confirm.pack()

    def open_create(self, master=None):
        self.login.pack_forget()
        self.create.pack_forget()

        self.msg_container = Frame(master)
        self.msg_container["pady"] = 10
        self.msg_container.pack()

        self.id_user_container = Frame(master)
        self.id_user_container["padx"] = 20
        self.id_user_container.pack()

        self.container1 = Frame(master)
        self.container1["padx"] = 20
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4.pack()

        self.address1_container = Frame(master)
        self.address1_container["padx"] = 20
        self.address1_container.pack()

        self.address2_container = Frame(master)
        self.address2_container["padx"] = 20
        self.address2_container.pack()

        self.address3_container = Frame(master)
        self.address3_container["padx"] = 20
        self.address3_container.pack()

        self.birthday_container = Frame(master)
        self.birthday_container["padx"] = 20
        self.birthday_container.pack()

        self.password_container = Frame(master)
        self.password_container["padx"] = 20
        self.password_container.pack()

        self.btn_container = Frame(master)
        self.btn_container["padx"] = 20
        self.btn_container["pady"] = 10
        self.btn_container.pack()

        self.msg_check = Frame(master)
        self.msg_check["pady"] = 10
        self.msg_check.pack()

        title = Label(self.msg_container, text="Informe os dados :", font=("Calibri", "9", "bold"))
        title.pack()

        name_Label = Label(self.container1, text="Nome:", font=self.font_pattern, width=8)
        name_Label.pack(side=LEFT)
        self.name = Entry(self.container1, width=25, font=self.font_pattern)
        self.name.pack(side=LEFT)

        CPF_Label = Label(self.container1, text="CPF:", font=self.font_pattern, width=8)
        CPF_Label.pack(side=LEFT)
        self.CPF = Entry(self.container1, width=12, font=self.font_pattern)
        self.CPF.pack(side=LEFT)

        name_mom_Label = Label(self.container2, text="Nome da mãe:", font=self.font_pattern, width=12)
        name_mom_Label.pack(side=LEFT)
        self.name_mom = Entry(self.container2, width=23, font=self.font_pattern)
        self.name_mom.pack(side=LEFT)

        CPF_mom_Label = Label(self.container2, text="CPF da mãe:", font=self.font_pattern, width=10)
        CPF_mom_Label.pack(side=LEFT)
        self.CPF_mom = Entry(self.container2, width=12, font=self.font_pattern)
        self.CPF_mom.pack(side=LEFT)

        RG_Label = Label(self.container3, text="RG:", font=self.font_pattern, width=6)
        RG_Label.pack(side=LEFT)
        self.RG = Entry(self.container3, width=12, font=self.font_pattern)
        self.RG.pack(side=LEFT)

        SUS_card_Label = Label(self.container3, text="Nº cartão SUS:", font=self.font_pattern, width=14)
        SUS_card_Label.pack(side=LEFT)
        self.SUS_card = Entry(self.container3, width=21, font=self.font_pattern)
        self.SUS_card.pack(side=LEFT)

        sex_Label = Label(self.container4, text="sexo:", font=self.font_pattern, width=4)
        sex_Label.pack(side=LEFT)
        self.sex = Entry(self.container4, width=12, font=self.font_pattern)
        self.sex.pack(side=LEFT)

        phone_Label = Label(self.container4, text="telefone:", font=self.font_pattern, width=6)
        phone_Label.pack(side=LEFT)
        self.phone = Entry(self.container4, width=12, font=self.font_pattern)
        self.phone.pack(side=LEFT)

        email_Label = Label(self.container4, text="Email:", font=self.font_pattern, width=5)
        email_Label.pack(side=LEFT)
        self.email = Entry(self.container4, width=17, font=self.font_pattern)
        self.email.pack(side=LEFT)

        city_Label = Label(self.address1_container, text="Cidade:", font=self.font_pattern, width=6)
        city_Label.pack(side=LEFT)
        self.city = Entry(self.address1_container, width=11, font=self.font_pattern)
        self.city.pack(side=LEFT)

        district_Label = Label(self.address1_container, text="Bairro:", font=self.font_pattern, width=6)
        district_Label.pack(side=LEFT)
        self.district = Entry(self.address1_container, width=11, font=self.font_pattern)
        self.district.pack(side=LEFT)

        road_Label = Label(self.address2_container, text="Rua:", font=self.font_pattern, width=6)
        road_Label.pack(side=LEFT)
        self.road = Entry(self.address2_container, width=11, font=self.font_pattern)
        self.road.pack(side=LEFT)

        number_Label = Label(self.address2_container, text="Numero:", font=self.font_pattern, width=6)
        number_Label.pack(side=LEFT)
        self.number = Entry(self.address2_container, width=11, font=self.font_pattern)
        self.number.pack(side=LEFT)

        complement_Label = Label(self.address3_container, text="Complemento:", font=self.font_pattern, width=10)
        complement_Label.pack(side=LEFT)
        self.complement = Entry(self.address3_container, width=25, font=self.font_pattern)
        self.complement.pack(side=LEFT)

        day_Label = Label(self.birthday_container, text="D:", font=self.font_pattern, width=2)
        day_Label.pack(side=LEFT)
        self.day = Entry(self.birthday_container, width=4, font=self.font_pattern)
        self.day.pack(side=LEFT)

        month_Label = Label(self.birthday_container, text="M:", font=self.font_pattern, width=2)
        month_Label.pack(side=LEFT)
        self.month = Entry(self.birthday_container, width=4, font=self.font_pattern)
        self.month.pack(side=LEFT)

        year_Label = Label(self.birthday_container, text="A:", font=self.font_pattern, width=2)
        year_Label.pack(side=LEFT)
        self.year = Entry(self.birthday_container, width=4, font=self.font_pattern)
        self.year.pack(side=LEFT)

        password_Label = Label(self.password_container, text="Senha:", font=self.font_pattern, width=10)
        password_Label.pack(side=LEFT)
        self.password = Entry(self.password_container, width=25, font=self.font_pattern, show="*")
        self.password.pack(side=LEFT)

        come_back_btn = Button(self.btn_container, text="Voltar", font=("Calibri", "12"), width=7)
        come_back_btn["command"] = self.come_back
        come_back_btn.pack(side=LEFT)

        create_btn = Button(self.btn_container, text="Criar", font=self.font_pattern, width=7)
        create_btn["command"] = self.create_confirm
        create_btn.pack(side=LEFT)

        self.msg_confirm = Label(self.msg_check, text="", font=self.font_pattern)
        self.msg_confirm.pack()

    def log_confirm(self):
        user = users()

        id_user = self.id_user.get()
        password = self.password.get()

        if user.selectUser(id_user, password):
            menu(id_user)

        else:
            self.msg_confirm["text"] = 'Senha ou usuário incorreto!'

    def create_confirm(self):
        user = users()

        user.name = self.name.get()
        user.name_mom = self.name_mom.get()
        user.CPF_mom = self.CPF_mom.get()
        user.CPF = self.CPF.get()
        user.RG = self.RG.get()
        user.SUS_card = self.SUS_card.get()
        user.sex = self.sex.get()
        user.phone = self.phone.get()
        user.email = self.email.get()
        user.password = self.password.get()

        user.city = self.city.get()
        user.district = self.district.get()
        user.road = self.road.get()
        user.number = self.number.get()
        user.complement = self.complement.get()

        user.day = self.day.get()
        user.month = self.month.get()
        user.year = self.year.get()

        self.msg_confirm["text"] = user.create_user()

        self.name.delete(0, END)
        self.name_mom.delete(0, END)
        self.CPF_mom.delete(0, END)
        self.CPF.delete(0, END)
        self.RG.delete(0, END)
        self.SUS_card.delete(0, END)
        self.sex.delete(0, END)
        self.phone.delete(0, END)
        self.email.delete(0, END)
        self.password.delete(0, END)

        self.city.delete(0, END)
        self.district.delete(0, END)
        self.road.delete(0, END)
        self.number.delete(0, END)
        self.complement.delete(0, END)

        self.day.delete(0, END)
        self.month.delete(0, END)
        self.year.delete(0, END)

    def come_back(self):
        self.login.pack(side=LEFT)
        self.create.pack(side=LEFT)
        self.msg_container.pack_forget()
        self.password_container.pack_forget()
        self.id_user_container.pack_forget()
        self.btn_container.pack_forget()
        self.container1.pack_forget()
        self.container2.pack_forget()
        self.container3.pack_forget()
        self.container4.pack_forget()
        self.msg_check.pack_forget()
        self.address1_container.pack_forget()
        self.address2_container.pack_forget()
        self.address3_container.pack_forget()
        self.birthday_container.pack_forget()

    def search_id(self, master=None):
        self.msg_container.pack_forget()
        self.msg_check.pack_forget()
        self.password_container.pack_forget()
        self.btn_container.pack_forget()
        self.id_user_container.pack_forget()

        self.msg_container = Frame(master)
        self.msg_container["pady"] = 10
        self.msg_container.pack()

        self.container1 = Frame(master)
        self.container1["padx"] = 20
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.password_container = Frame(master)
        self.password_container["padx"] = 20
        self.password_container.pack()

        self.btn_container = Frame(master)
        self.btn_container["padx"] = 20
        self.btn_container["pady"] = 10
        self.btn_container.pack()

        self.msg_check = Frame(master)
        self.msg_check["pady"] = 10
        self.msg_check.pack()

        title = Label(self.msg_container, text="Informe os dados :", font=("Calibri", "9", "bold"))
        title.pack()

        name_Label = Label(self.container1, text="Nome:", font=self.font_pattern, width=10)
        name_Label.pack(side=LEFT)
        self.name = Entry(self.container1, width=25, font=self.font_pattern)
        self.name.pack(side=LEFT)

        CPF_Label = Label(self.container2, text="CPF:", font=self.font_pattern, width=10)
        CPF_Label.pack(side=LEFT)
        self.CPF = Entry(self.container2, width=25, font=self.font_pattern)
        self.CPF.pack(side=LEFT)

        password_Label = Label(self.password_container, text="Senha:", font=self.font_pattern, width=10)
        password_Label.pack(side=LEFT)
        self.password = Entry(self.password_container, width=25, font=self.font_pattern, show="*")
        self.password.pack(side=LEFT)

        come_back_btn = Button(self.btn_container, text="Voltar", font=("Calibri", "12"), width=7)
        come_back_btn["command"] = self.come_back
        come_back_btn.pack(side=LEFT)

        create_btn = Button(self.btn_container, text="Procurar", font=self.font_pattern, width=7)
        create_btn["command"] = self.search
        create_btn.pack(side=LEFT)

        self.msg_confirm = Label(self.msg_check, text="", font=self.font_pattern)
        self.msg_confirm.pack()

    def search(self):
        user = users()

        user.name = self.name.get()
        user.CPF = self.CPF.get()
        user.password = self.password.get()

        self.msg_confirm["text"] = user.search_id()

        self.name.delete(0, END)
        self.CPF.delete(0, END)
        self.password.delete(0, END)


root = Tk()
Application(root)
root.mainloop()
