from main import *

from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("personalfinance tracker")
root.geometry("500x500")

#accounts menu
def account_menu():

    def change_pin_menu():

        b4.destroy()
        b5.destroy()
        b6.destroy()
        b7.destroy()

        l2 = Label(root, text="old pin")
        l2.pack()

        e2 = Entry(root, width=25)
        e2.pack()

        l3 = Label(root, text="new pin")
        l3.pack()

        e3 = Entry(root, width=25)
        e3.pack()

        l4 = Label(root, text="re-enter pin")
        l4.pack()

        e4 = Entry(root, width=25)
        e4.pack()

        b15 = Button(root, text="CHANGE", width=25)
        b15.pack()
        def back():
            l2.destroy()
            e2.destroy()
            l3.destroy()
            e3.destroy()
            l4.destroy()
            e4.destroy()
            b15.destroy()
            b16.destroy()
            account_menu()

        b16 = Button(root, text="BACK", width="25", command=back)
        b16.pack()


    def details_menu():
        pass

    #deposit menu
    def deposit_menu():
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b7.destroy()

        l1 = Label(root, text="AMOUNT")
        l1.pack()

        e1 = Entry(root, width=25)
        e1.pack()

        b13 = Button(root, text="DEPOSIT", width=25)
        b13.pack()

        def back():
            l1.destroy()
            e1.destroy()
            b13.destroy()
            b14.destroy()
            account_menu()

        b14 = Button(root, text="BACK", width="25", command=back)
        b14.pack()

    b1.destroy()
    b2.destroy()
    b3.destroy()

    b4 = Button(root,text="DEPOSIT MONEY", width="25", command=deposit_menu)
    b4.pack()

    b5 = Button(root, text="CHANGE PIN", width="25", command=change_pin_menu)
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


#savings menu
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

#expense menu
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


#main menu
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

