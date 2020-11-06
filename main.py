from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
import mysql.connector as sqltor
from passlib.hash import pbkdf2_sha256
import random
import smtplib
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem
import pymysql


class Login_Page(Screen):
    pass


class Signup_Page(Screen):
    pass

class OTP_Page(Screen):
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


class OTP_Login(Screen):
    pass


class OTP_Signup(Screen):
    pass


class OTP_Transfer(Screen):
    pass


class OTP_Withdraw(Screen):
    pass


class OTP_Deposit(Screen):
    pass

class Transaction_Success(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        screen = Builder.load_file("my.kv")
        return screen


    def credential_check(self, user_acc_no, password):
        mycon = sqltor.connect(host="sql12.freesqldatabase.com", user="sql12374879", passwd="JwmHqPqM4q", database="sql12374879")
        cursor = mycon.cursor()
        user_acc_no_sql = str("('" + user_acc_no + "',)")
        cursor.execute("SELECT ACC_NO FROM USERS1010;")
        acc_check = 0
        for i in cursor:
            if user_acc_no_sql == str(i):
                acc_check = 1

        cursor.execute("SELECT PASSWORD FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(user_acc_no))
        for row in cursor.fetchall():
            for i in row:
                crypt = i
        credential_check = pbkdf2_sha256.verify(password, crypt)
        return credential_check

    def success_dialog(self,user_acc_no, password):
        mycon = sqltor.connect(host="sql12.freesqldatabase.com", user="sql12374879", passwd="JwmHqPqM4q", database="sql12374879")
        cursor = mycon.cursor()
        user_acc_no_sql = str("('" + user_acc_no + "',)")
        cursor.execute("SELECT ACC_NO FROM USERS1010;")
        acc_check = 0
        for i in cursor:
            if user_acc_no_sql == str(i):
                acc_check = 1

        cursor.execute("SELECT PASSWORD FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(user_acc_no))
        for row in cursor.fetchall():
            for i in row:
                crypt = i
        credential_check = pbkdf2_sha256.verify(password, crypt)
        if credential_check == True:
            mycon = sqltor.connect(host="sql12.freesqldatabase.com", user="sql12374879", passwd="JwmHqPqM4q", database="sql12374879")
            cursor = mycon.cursor()
            st = "select BALANCE from USERS1010 where ACC_NO='%s'" % (user_acc_no)
            cursor.execute(st)
            data = cursor.fetchall()
            for row in data:
                balance = row[0]
            balance = str(balance)
            balance_string = "Current Balance is " + chr(8377) + balance
            self.dialog = MDDialog(title=balance_string, size_hint=(0.7, 1), buttons=[
                                MDRaisedButton(text='OK', on_release= self.close_dialog)])
            self.dialog.open()
    def close_dialog(self,user_acc_no):
        self.dialog.dismiss()

    def signup_new(self, name, surname, pswd, ph_no, adr_no, email):
        mycon = sqltor.connect(host="sql12.freesqldatabase.com", user="sql12374879", passwd="JwmHqPqM4q", database="sql12374879")
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
            cursor.execute("SELECT ACC_NO FROM USERS1010;")
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
        acc_string = "Your Account number is " + acc_no
        self.dialog = MDDialog(title=acc_string, text="Please note this down for future purposes", size_hint=(0.7, 1), buttons=[
                                MDRaisedButton(text='OK', on_release= self.close_dialog)])

        self.dialog.open()
        global user
        user = acc_no
        cursor.execute(
            "INSERT INTO USERS1010( ACC_NO , NAME , SURNAME , PHONE_NUMBER , BALANCE , PASSWORD , AADHAR_NUMBER, EMAIL) VALUES({},'{}','{}',{},{},'{}',{} , '{}');".format(
                acc_no, name, surname, ph_no, balance, pswd, adr_no, email))
        mycon.commit()


    def log1(self,email):
        global r
        r = " "
        for i in range(0, 5):
            a = random.randint(0, 9)
            a = str(a)
            r = r + a

        fromaddr = 'pybankcustomer@gmail.com'
        toaddrs = str(email)
        username = 'pybankcustomer@gmail.com'
        password = '8uhb9ijn'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, "Your OTP is " + str("") + r)
        server.quit()

    def log(self, acc_no):
        mycon = sqltor.connect(host="sql12.freesqldatabase.com", user="sql12374879", passwd="JwmHqPqM4q", database="sql12374879")
        cursor = mycon.cursor()
        st = "select EMAIL from USERS1010 where ACC_NO='%s'" % (acc_no)
        cursor.execute(st)
        data = cursor.fetchall()
        for row in data:
            email = row[0]

        global r
        r = " "
        for i in range(0, 5):
            a = random.randint(0, 9)
            a = str(a)
            r = r + a

        fromaddr = 'pybankcustomer@gmail.com'
        toaddrs = str(email)
        username = 'pybankcustomer@gmail.com'
        password = '8uhb9ijn'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, "Your OTP is " + str("") + r)
        server.quit()

    def chec(self, passw):
        if str(passw) == r.strip():
            return True
        else:
            return False

    def withdraw(self, acc_no, pswd, amt):
        mycon = sqltor.connect(host="sql12.freesqldatabase.com", user="sql12374879", passwd="JwmHqPqM4q", database="sql12374879")
        cursor = mycon.cursor()
        cursor.execute("SELECT PASSWORD FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(acc_no))
        for row in cursor.fetchall():
            for i in row:
                crypt = i
        credential_check = pbkdf2_sha256.verify(pswd, crypt)
        if credential_check == True:
            st = "UPDATE USERS1010 SET balance=balance-{} WHERE ACC_NO={}".format(amt, acc_no)
            cursor.execute(st)
            mycon.commit()

    def deposit(self, acc_no, pswd, amt):
        mycon = sqltor.connect(host="sql12.freesqldatabase.com", user="sql12374879", passwd="JwmHqPqM4q", database="sql12374879")
        cursor = mycon.cursor()
        cursor.execute("SELECT PASSWORD FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(acc_no))
        for row in cursor.fetchall():
            for i in row:
                crypt = i
        credential_check = pbkdf2_sha256.verify(pswd, crypt)
        if credential_check == True:
            st = "UPDATE USERS1010 SET balance=balance+{} WHERE ACC_NO={}".format(amt, acc_no)
            cursor.execute(st)
            mycon.commit()

    def transfer(self, acc_no, t_acc_no, pswd, amt):
        mycon = sqltor.connect(host="sql12.freesqldatabase.com", user="sql12374879", passwd="JwmHqPqM4q", database="sql12374879")
        cursor = mycon.cursor()
        cursor.execute("SELECT PASSWORD FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(acc_no))
        for row in cursor.fetchall():
            for i in row:
                crypt = i
        credential_check = pbkdf2_sha256.verify(pswd, crypt)
        if credential_check == True:
            st = "UPDATE USERS1010 SET balance=balance+{} WHERE ACC_NO={}".format(amt, t_acc_no)
            cursor.execute(st)
            mycon.commit()
            st = "UPDATE USERS1010 SET balance=balance-{} WHERE ACC_NO={}".format(amt, acc_no)
            cursor.execute(st)
            mycon.commit()


MyApp().run()
