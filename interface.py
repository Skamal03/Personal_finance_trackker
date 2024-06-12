from main import *

from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("personalfinance tracker")
root.geometry("500x500")

def account_menu():
    b1.destroy()
    b2.destroy()
    b3.destroy()

    b4 = Button(root,text="DEPOSIT MONEY", width="25")
    b4.pack()

    b5 = Button(root, text="CHANGE PIN", width="25")
    b5.pack()

    b6 = Button(root, text="CHECK DETAILS", width="25")
    b6.pack()

    def back():
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b7.destroy()
        main()

    b7 = Button(root, text="Back",command=back, width="25")
    b7.pack()

    def deposit_menu():
        l1 = Label(root, text="AMOUNT")
        l1.pack()
        e1 = Entry(root,width=30)
        e1.pack()

    def change_pin_menu():
        pass

def savings_menu():
    b1.destroy()
    b2.destroy()
    b3.destroy()

    b7 = Button(root, text="DEPOSIT IN SAVINGS", width=25,)
    b7.pack()

    b8 = Button(root, text="SEE INFO", width=25)
    b8.pack()

    def back():
        b7.destroy()
        b8.destroy()
        b9.destroy()
        main()

    b9 = Button(root, text="Back",command=back, width=25)
    b9.pack()


def expense_menu():
    b1.destroy()
    b2.destroy()
    b3.destroy()

    e1 = Entry(root, )

    b9 = Button(root, text="ADD EXPENSE", width=25,)
    b9.pack()

    b10 = Button(root, text="REMOVE EXPENSE", width=25)
    b10.pack()

    b11 = Button(root, text="DISPLAY EXPENSE", width=25)
    b11.pack()

    def back():
        b9.destroy()
        b10.destroy()
        b11.destroy()
        b12.destroy()
        main()

    b12 = Button(root, text="Back",command=back, width=25)
    b12.pack()

    def add_expensse_menu():
        pass

    def delete_expense_menu():
        pass

    def dispaly_expense_menu():
        pass


def main():
    global b1,b2,b3
    b1 = Button(root, text="ACCOUNT", width="25", command=account_menu)
    b1.pack()
    b2 = Button(root, text="SAVINGS", width="25", command=savings_menu)
    b2.pack()
    b3 = Button(root, text="EXPENSE", width="25", command=expense_menu)
    b3.pack()


b1 = Button(root,text="ACCOUNT", width="25", command=account_menu)
b1.pack()
b2 = Button(root, text="SAVINGS", width="25", command=savings_menu)
b2.pack()
b3 = Button(root, text="EXPENSE", width="25", command=expense_menu)
b3.pack()

root.mainloop()

