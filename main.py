from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
import mysql.connector as sqltor
from passlib.hash import pbkdf2_sha256
from kivymd.uix.list import OneLineIconListItem
import pymysql

class Login_Page(Screen):
    pass


class Signup_Page(Screen):
    pass


class Home(Screen):
    pass


class Balance(Screen):
    pass


class Withdraw(Screen):
    pass


class Deposit(Screen):
    pass


class Transfer(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        screen = Builder.load_file("my.kv")
        return screen




    def credential_check(self, user_acc_no, password):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
        cursor = mycon.cursor()
        user_acc_no_sql = str("('" + user_acc_no + "',)")
        cursor.execute("SELECT ACC_NO FROM USERS101;")
        acc_check = 0
        for i in cursor:
            if user_acc_no_sql == str(i):
                acc_check = 1

        cursor.execute("SELECT PASSWORD FROM USERS101 WHERE ACC_NO LIKE '{}';".format(user_acc_no))
        for row in cursor.fetchall():
            for i in row:
                crypt = i
        credential_check = pbkdf2_sha256.verify(password, crypt)

        return credential_check


    def get_withdraw_amount(self, amount):
        print(amount)

    def upload_success_dialog(self):
        balance=str(1234)
        balance_string="Current Balance is "+ chr(8377) +balance
        dialog = MDDialog(title=balance_string, size_hint=(0.7, 1))
        dialog.open()

    def signup_new(self, name, surname, pswd, ph_no, adr_no):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
        cursor = mycon.cursor()
        import random
        check = 0
        while check == 0:
            acc_no = ""
            for i in range(0, 10):
                a = random.randint(0, 9)
                a = str(a)
                acc_no = acc_no + a

            user_acc_no_sql = str("('" + acc_no + "',)")
            cursor.execute("SELECT ACC_NO FROM USERS101;")
            acc_check = 0
            for i in cursor:
                if user_acc_no_sql == str(i):
                    acc_check = 1
                else:
                    continue

            if acc_check == 1:
                check = 0
            else:
                check = 1
        balance = 0
        pswd = pbkdf2_sha256.hash(pswd)
        cursor.execute(
            "INSERT INTO USERS101( ACC_NO , NAME , SURNAME , PHONE_NUMBER , BALANCE , PASSWORD , AADHAR_NUMBER) VALUES({},'{}','{}',{},{},'{}',{});".format(
                acc_no, name, surname, ph_no, balance, pswd, adr_no))
        mycon.commit()


MyApp().run()
