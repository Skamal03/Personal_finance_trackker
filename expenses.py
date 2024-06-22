from tkinter import messagebox
from abc import ABC, abstractmethod
import mysql.connector
import csv


class Accounts(ABC):

    @abstractmethod
    def deposit_amount(self, amount):
        pass

    def retrieve(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

class UserAccount(Accounts):

    def __init__(self, account_balance=0000, account_name="USER", account_number=5680456754, account_pin=4269):
        self.acc_name = account_name
        self.acc_no = account_number
        self.acc_balance = account_balance
        self.__acc_pin = account_pin

    def retrive(self):

        with open("balance.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            last_row = rows[-1]

            self.acc_balance = int(last_row[3])

    def withdraw(self, amount, date, pin):

        if pin == user_account.__acc_pin:

            if amount <= self.acc_balance:
                self.acc_balance -= amount
                messagebox.showinfo("SUCCESS", "Amount successfully withdrawn!")

                with open("balance.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([date, 0, amount, self.acc_balance])

            else:
                messagebox.showerror("Fail", "Not enough money to Withdraw")

        else:
            messagebox.showerror("ERROR", "Wrong PIN")

    def deposit_amount(self, amount, date):

        if isinstance(amount, int):
            self.acc_balance += amount
            messagebox.showinfo("SUCCESS", "Amount successfully deposited!")

            with open("balance.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([date, amount, 0, self.acc_balance])


        else:
            messagebox.showinfo("FAIL", "enter correct values")


    def get_details(self):
        messagebox.showinfo("DETAILS", f"Account Name:{self.acc_name}\nAccount Number: {self.acc_no}"
                                       f"\nAccount Balance: {self.acc_balance}")

class Savings:

    def __init__(self, user_account, savings=00):
        self.user_account = user_account
        self.savings = savings

    def retrive(self):

        with open("Savings_deposit.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            last_row = rows[-1]

            self.savings = int(last_row[2])

    def deposit_amount(self, deposit, date):

        if isinstance(deposit,str):
            messagebox.showerror("ERROR","Invalid entry")

        elif deposit > self.user_account.acc_balance:
            messagebox.showwarning("WARNING","Invalid amount. Not enough balance in your account.")

        else:
            self.user_account.acc_balance -= deposit
            self.savings += deposit
            messagebox.showinfo("SUCCESS","Amount successfully deposited in savings!")

            with open("Savings_deposit.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([date, deposit, self.savings])

    def get_details(self):
        messagebox.showinfo("DETAILS", f"Account Name:{self.user_account.acc_name}\nAccount Number: {self.user_account.acc_no}"
                                       f"\nAccount Balance: {self.user_account.acc_balance}\nSavings Balance{self.savings}")

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

    def get_category(self, category):
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

        try:
            expense_id = id
            query = "DELETE FROM expenses WHERE id=%s"
            mycursor.execute(query, (expense_id,))
            mydb.commit()
            mydb.close()

            print("Expense successfully deleted!")

        except:
            messagebox.showerror("ERROR", "invalid expense id")


user_account = UserAccount()
savings = Savings(user_account)
expense = Expense(user_account, savings)
