from tkinter import messagebox
from abc import ABC, abstractmethod
import mysql.connector


class Accounts(ABC):

    @abstractmethod
    def deposit_amount(self, amount):
        pass

    @abstractmethod
    def get_details(self):
        pass

class UserAccount(Accounts):

    def __init__(self, account_balance=000, account_number=5680456754, account_pin=0000):
        self.acc_no = account_number
        self.acc_balance = account_balance
        self.__acc_pin = account_pin

    def deposit_amount(self, amount):

        if isinstance(amount, int):
            self.acc_balance += amount
            messagebox.showinfo("SUCCESS", "Amount successfully deposited!")

        else:
            messagebox.showinfo("FAIL", "enter correct values")

    def set_pin(self, old_pin, new_pin):

        if old_pin == self.__acc_pin:

            self.__acc_pin = new_pin
            messagebox.showinfo("SUCCESS", "pin changed successfully")

        else:

            messagebox.showinfo("WARNING", "you entered wrong pin!")

    def get_details(self):
        messagebox.showinfo("DETAILS", f"Account Number: {self.acc_no}\nAccount Balance: {self.acc_balance}")


class Savings:

    def __init__(self, user_account, savings=0):
        self.user_account = user_account
        self.savings = savings

    def deposit_amount(self, deposit):

        if isinstance(deposit,str):
            messagebox.showerror("ERROR","Invalid entry")

        elif deposit > self.user_account.acc_balance:
            messagebox.showwarning("WARNING","Invalid amount. Not enough balance in your account.")

        else:
            self.user_account.acc_balance -= deposit
            self.savings += deposit
            messagebox.showinfo("SUCCESS","Amount successfully deposited in savings!")

    def get_details(self):
        messagebox.showinfo("DETAILS",f"Account Number: {self.user_account.acc_no}\nAccount Balance: {self.user_account.acc_balance}"
                f"\nSavings Balance: {self.savings}")

class Expense:

    def __init__(self, user_account, savings, name="", category="", amount=0.00, date="00-00-0000"):
        self.user_account = user_account
        self.savings = savings
        self.category = category
        self.amount = amount
        self.date = date
        self.name = name

    def get_name(self,name):
        self.name = name

    def get_category(self,category):
        self.category = category

    def get_date(self,date):
        self.date = date

    def get_amount(self, amount):
        self.amount = amount

    def save_to_database(self):

        if self.amount > self.user_account.acc_balance:
            answer = messagebox.askyesno("ERROR","Not enough balance\nDo you want to use savings?")

            if answer:
                if self.amount > (self.user_account.acc_balance + self.savings.savings):
                    messagebox.showinfo("ERROR","Not enough balance in savings.")
                    return
                else:
                    self.savings.savings -= (self.amount - self.user_account.acc_balance)
                    self.user_account.acc_balance = 0
            else:
                return
        else:
            self.user_account.acc_balance -= self.amount


        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="6090",
            database="expense"
        )
        mycursor = mydb.cursor()

        query = "INSERT INTO expenses (name, amount, date, type) VALUES (%s, %s, %s, %s)"
        val = (self.name, self.amount, self.date, self.category)

        mycursor.execute(query, val)
        mydb.commit()
        mydb.close()

        print("Expense successfully saved!")

    def delete_expense(self,id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="6090",
            database="expense"
        )
        mycursor = mydb.cursor()

        expense_id = id
        query = "DELETE FROM expenses WHERE id=%s"
        mycursor.execute(query, (expense_id,))
        mydb.commit()
        mydb.close()

        print("Expense successfully deleted!")

    def display_expenses(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="6090",
            database="expense"
        )
        mycursor = mydb.cursor()

        query = "SELECT * FROM expenses"
        mycursor.execute(query)
        records = mycursor.fetchall()

        for record in records:
            print(record)

        mydb.close()


user_account = UserAccount()
savings = Savings(user_account)
expense = Expense(user_account, savings)
