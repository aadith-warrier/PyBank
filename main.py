from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
import mysql.connector as sqltor
from passlib.hash import pbkdf2_sha256
import random
import smtplib
from email.message import EmailMessage
from datetime import datetime
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem
import pymysql

class Welcome_Page(Screen):
    pass

class Admin_Page(Screen):
    pass

class Login_Page(Screen):
    pass


class Signup_Page(Screen):
    pass

class OTP_Page(Screen):
    pass

class Admin_Home(Screen):
    pass

class Customer_Details(Screen):
    pass

class Customer_Contact(Screen):
    pass

class Home(Screen):
    pass

class Trans_Hist(Screen):
    pass

class FB(Screen):
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

class Transaction_Success(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        screen = Builder.load_file("my.kv")
        return screen


    def credential_check(self, user_acc_no, password):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
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

    def credential_check_admin(self, acc_no, password):
        if int(acc_no) == 1234567890 and str(password) == "admin@123":
            return True
        else:
            return False

    def success_dialog(self,user_acc_no, password):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
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
            mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
            cursor = mycon.cursor()
            st = "select BALANCE from USERS1010 where ACC_NO='%s'" % (user_acc_no)
            cursor.execute(st)
            data = cursor.fetchall()
            for row in data:
                balance = str(row[0])
            balance_string = "Current Balance is " + chr(8377) + balance

            self.dialog = MDDialog(title=balance_string, size_hint=(0.7, 1), buttons=[
                                MDRaisedButton(text='OK', on_release= self.close_dialog)])
            self.dialog.open()

    def trans_dialog(self,user_acc_no, password):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
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
            mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
            cursor = mycon.cursor()

            st= "select * from trans_bank50 where to1='%s'" %(user_acc_no)
            cursor.execute(st)
            data = cursor.fetchall()
            l=[]
            l3=[]
            for row in data:
                if row[0] == " ":
                    a3= str(row[3])
                    a2= str(row[2])
                    a = "Deposit of Rs" + " " + a2 + " " + "at" + " " + a3
                    l.append(a)

                else:
                    a3 = str(row[3])
                    a2 = str(row[2])
                    a0=row[0]
                    a = "Receipt of Rs" + " " + a2 + " " + "from" + " " + a0 + " " + "at" + " " + a3
                    l3.append(a)

            st = "select * from trans_bank50 where from1='%s'" % (user_acc_no)
            cursor.execute(st)
            data = cursor.fetchall()
            l2 = []
            l4=[]
            for row in data:
                if row[1] == " ":
                    a3 = str(row[3])
                    a2 = str(row[2])
                    a = "Withdrawal of Rs" + \
                        " " + a2 + " " + "at" + " " + a3
                    l2.append(a)

                else:
                    a3 = str(row[3])
                    a2 = str(row[2])
                    a1 = row[1]
                    a = "Transfer of Rs" + " " + a2 + " " + "to" +" " + a1 + " " + "at" + " " + a3
                    l4.append(a)


            b="DEPOSITS"
            for i in l:
                b = b +"\n" + i

            c = "WITHDRAWALS"
            b= b + 2*"\n" + c
            for i in l2:
                b = b + "\n" + i

            c1 = "TRANSFERS"
            b = b + 2*"\n" + c1
            for i in l3:
                b = b + "\n" + i
            for i in l4:
                b = b + "\n" + i

            st = "select BALANCE from USERS1010 where ACC_NO='%s'" % (user_acc_no)
            cursor.execute(st)
            data = cursor.fetchall()
            for row in data:
                balance1 = str(row[0])
            b = b + 2*"\n" + "Current Balance: " + " " + balance1
            balance= str(b)
            balance_string = balance
            self.dialog = MDDialog(title="Transaction History", text=balance_string, size_hint=(0.7, 1), buttons=[
                                MDRaisedButton(text='OK', on_release= self.close_dialog)])
            self.dialog.open()

    def feedback_dialog(self, email, password, feedback):
        feedback = str(feedback)
        msg = EmailMessage()
        msg.set_content(feedback)

        msg['Subject'] = 'Feedback'
        msg['From'] = str(email)
        msg['To'] = 'pybankcustomer@gmail.com'
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(str(email), str(password))
        server.send_message(msg)
        server.quit()

        self.dialog = MDDialog(title="Feedback Sent", size_hint=(0.7, 1), buttons=[
            MDRaisedButton(text='OK', on_release=self.close_dialog)])
        self.dialog.open()


    def close_dialog(self,user_acc_no):
        self.dialog.dismiss()

    def signup_new(self, name, surname, pswd, ph_no, adr_no, email):
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
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
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

    def details(self, acc_no):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
        cursor = mycon.cursor()
        cursor.execute("SELECT NAME FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(acc_no))
        data = cursor.fetchall()
        for row in data:
            name = row[0]

        cursor.execute("SELECT SURNAME FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(acc_no))
        data = cursor.fetchall()
        for row in data:
            surname = row[0]

        cursor.execute("SELECT PHONE_NUMBER FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(acc_no))
        data = cursor.fetchall()
        for row in data:
            ph = row[0]

        cursor.execute("SELECT AADHAR_NUMBER FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(acc_no))
        data = cursor.fetchall()
        for row in data:
            aadn = row[0]

        cursor.execute("SELECT EMAIL FROM USERS1010 WHERE ACC_NO LIKE '{}';".format(acc_no))
        data = cursor.fetchall()
        for row in data:
            email = row[0]

        c = "Customer Details"
        b = "Account Number: " + " " + str(acc_no)
        b = b + "\n"+ "First Name: " + " " + str(name)
        b = b + "\n" + "Last Name: " + " " + str(surname)
        b = b + "\n" + "Phone Number: " + " " + str(ph)
        b = b + "\n" + "Aadhar Number: " + " " + str(aadn)
        b = b + "\n" + "Email: " + " " + str(email)

        self.dialog = MDDialog(title=str(c), text=str(b), size_hint=(0.7, 1),buttons=[
                                   MDRaisedButton(text='OK', on_release=self.close_dialog)])

        self.dialog.open()

    def contact(self, acc_no, message):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
        cursor = mycon.cursor()
        st = "select EMAIL from USERS1010 where ACC_NO='%s'" % (acc_no)
        cursor.execute(st)
        data = cursor.fetchall()
        for row in data:
            email = row[0]

        fromaddr = 'pybankcustomer@gmail.com'
        toaddrs = str(email)
        username = 'pybankcustomer@gmail.com'
        password = '8uhb9ijn'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, str(message))
        server.quit()

    def withdraw(self, acc_no, pswd, amt):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
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
            st0 = "select balance from USERS1010 where ACC_NO='%s'" % (acc_no)
            cursor.execute(st0)
            data = cursor.fetchall()
            for row in data:
                balance = row[0]
            now = datetime.now()
            now = str(now)
            c = " "
            st1 = " INSERT INTO trans_bank50(from1,to1,amount,datetime1,balance) VALUES('{}','{}',{},'{}',{})".format(acc_no,c, amt, now, balance)
            cursor.execute(st1)
            mycon.commit()

    def deposit(self, acc_no, pswd, amt):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
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
            st0 = "select balance from USERS1010 where ACC_NO='%s'" % (acc_no)
            cursor.execute(st0)
            data = cursor.fetchall()
            for row in data:
                balance = row[0]
            now = datetime.now()
            now = str(now)
            c = " "
            st1 = " INSERT INTO trans_bank50(from1,to1,amount,datetime1,balance) VALUES('{}','{}',{},'{}',{})".format(c,acc_no,amt,now,balance)
            cursor.execute(st1)
            mycon.commit()

    def transfer(self, acc_no, t_acc_no, pswd, amt):
        mycon = sqltor.connect(host="localhost", user="root", passwd="markbottle$2003", database="users")
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
            st0 = "select balance from USERS1010 where ACC_NO='%s'" % (acc_no)
            cursor.execute(st0)
            data = cursor.fetchall()
            for row in data:
                balance = row[0]
            now = datetime.now()
            now = str(now)
            c = " "
            st1 = " INSERT INTO trans_bank50(from1,to1,amount,datetime1,balance) VALUES('{}','{}',{},'{}',{})".format(acc_no,t_acc_no,amt,now,balance)
            cursor.execute(st1)
            mycon.commit()

MyApp().run()
