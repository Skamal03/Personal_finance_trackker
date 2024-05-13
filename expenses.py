import csv
class Expense:

    def __init__(self,name="", category="", amount=00, date="00-00-0000"):
        self.category = category
        self.amount = amount
        self.date = date
        self.name = name

    def get_name(self):
        name = input("Enter name of an expense=")
        self.name = name

    def get_category(self):
        while True:

            print("Select from above option")
            print(f" 1.Food\n 2.Rent\n 3.Bill\n 4.Miscellaneous")
            category = int(input("enter a category="))

            if category == 1:
                self.category = "Food"
                break

            if category == 2:
                self.category = "Rent"
                break

            if category == 3:
                self.category = "Bill"
                break

            if category == 4:
                self.category = "Miscellaneous"
                break

            if category >= 5:
                print("=====wrong input, please enter again!======")

    def get_amount(self):

        amount = int(input("enter an amount="))
        self.amount = amount

    def get_date(self):

        date = input("enter the date(DD-MM-YYYY)=")
        self.date = date

    def save_to_file(self, filename="expenses1.csv"):

            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.category, self.date, self.amount])
                print("=====Expenses saved successfully!=====")

    def display_expenses(self):
        pass

class Accounts:

    def __init__(self, account_balance, account_pin):
        self.__acc_balance = account_balance
        self.__acc_pin = account_pin

    def set_pin(self):

        pin = input("Set your pin=")
        self.__acc_pin = pin


    def set_account_balance(self):
        self.balance=int(input("enter accout balance="))


class Savings(Accounts):

    def deposit(self):
        savings=0
        deposit=int(input("enter an amount to deposit"))

        if deposit > self.balance:
            print("invalid amount\n dont have enough amount in your account")
        else:
            savings += deposit

if __name__ == "__main__":

    expense = Expense()


while True:
    print("1.Add expense")
    print("3.display expense")
    print("4.exit")
    print("5.deposit amount to savings")

    option=int(input("choose from above option="))

    if option == 1:
        expense.get_category()
        expense.get_name()
        expense.get_amount()
        expense.get_date()
        expense.save_to_file()
        break

