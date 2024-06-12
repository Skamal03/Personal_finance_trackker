from abc import ABC, abstractmethod
import mysql.connector

class Accounts(ABC):

    @abstractmethod
    def deposit_in_account(self):
        pass

    @abstractmethod
    def set_pin(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

class UserAccount(Accounts):

    def __init__(self, account_number=567890123, account_balance=0.00, account_pin=0000):
        self.acc_no = account_number
        self.acc_balance = account_balance
        self.__acc_pin = account_pin

    def deposit_in_account(self,):

        amount = int(input("enter amount to deposit"))
        self.acc_balance += amount
        print("Amount successfully deposited!")


    def set_pin(self):

        pin = int(input("Enter your pin: "))
        tries = 0

        while tries <= 3 :

            if pin == self.__acc_pin:
                new_pin = int(input("Enter new pin"))
                new_pin = self.__acc_pin

            else:
                tries += 1
                print("Wrong pin! you have", tries, "left")


    def get_details(self):
        return f"Account Number: {self.acc_no}\nAccount Balance: {self.acc_balance}"

class Savings:

    def __init__(self, user_account, savings=0):
        self.user_account = user_account
        self.savings = savings

    def deposit_in_savings(self):
        deposit = float(input("Enter an amount to deposit in savings: "))

        if deposit > self.user_account.acc_balance:
            print("Invalid amount. Not enough balance in your account.")
        else:
            self.user_account.acc_balance -= deposit
            self.savings += deposit
            print("===== Amount successfully deposited in savings! =====")

    def get_details(self):
        return f"Account Number: {self.user_account.acc_no}\nAccount Balance: {self.user_account.acc_balance}\nSavings Balance: {self.savings}"

class Expense:

    def __init__(self, user_account, savings, name="", category="", amount=0.00, date="00-00-0000"):
        self.user_account = user_account
        self.savings = savings
        self.category = category
        self.amount = amount
        self.date = date
        self.name = name

    def get_name(self):
        self.name = input("Enter name of the expense: ")

    def get_category(self):
        while True:
            print("Select a category from the options below:")
            print(" 1. Food\n 2. Rent\n 3. Bill\n 4. Miscellaneous")
            category = int(input("Enter a category number: "))

            if category == 1:
                self.category = "Food"
                break
            elif category == 2:
                self.category = "Rent"
                break
            elif category == 3:
                self.category = "Bill"

            elif category == 4:
                self.category = "Clothing"
                break

            elif category == 5:
                self.category = "Miscellaneous"
                break
            else:
                print("===== Wrong input, please enter again! =====")

    def get_date(self):
        self.date = input("Enter the date (DD-MM-YYYY): ")

    def get_amount(self):
        self.amount = float(input("Enter the amount: "))

    def save_to_database(self):

        if self.amount > self.user_account.acc_balance:
            print("Not enough balance.")
            use_savings = input("Use savings? (Y/N): ")

            if use_savings.lower() == 'y':
                if self.amount > (self.user_account.acc_balance + self.savings.savings):
                    print("Not enough balance in savings.")
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

        print("===== Expense successfully saved! =====")

    def delete_expense(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="6090",
            database="expense"
        )
        mycursor = mydb.cursor()

        expense_id = int(input("Enter expense ID to delete: "))
        query = "DELETE FROM expenses WHERE id=%s"
        mycursor.execute(query, (expense_id,))
        mydb.commit()
        mydb.close()

        print("===== Expense successfully deleted! =====")

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

        for expense in mycursor:
            print(expense)

        mydb.close()

if __name__ == "__main__":
    user_account = UserAccount()
    savings = Savings(user_account)
    expense = Expense(user_account, savings)
    user_account.deposit_in_account()


    print(user_account.get_details())
    savings.deposit_in_savings()
    print(savings.get_details())
    expense.get_name()
    expense.get_category()
    expense.get_date()
    expense.get_amount()
    expense.save_to_database()
    expense.display_expenses()
