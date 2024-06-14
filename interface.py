from main import *
from tkinter import *

root = Tk()

root.title("personalfinance tracker")
root.geometry("500x500")

#accounts menu
def account_menu():

    b1.destroy()
    b2.destroy()
    b3.destroy()

    global b4, b5, b6, b7
    b4 = Button(root,text="DEPOSIT MONEY", width="25", command=deposit_menu)
    b4.pack()

    b5 = Button(root, text="CHANGE PIN", width="25", command=change_pin_menu)
    b5.pack()

    b6 = Button(root, text="CHECK DETAILS", width="25", command=user_account.get_details)
    b6.pack()

    def back():
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b7.destroy()
        main()

    b7 = Button(root, text="Back",command=back, width="25")
    b7.pack()

# deposit menu
def deposit_menu():

    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()

    l1 = Label(root, text="AMOUNT")
    l1.pack()

    global amount_entry
    amount_entry= Entry(root, width=25)
    amount_entry.pack()

    b13 = Button(root, text="DEPOSIT", width=25, command=handling_deposit)
    b13.pack()

    def back():
        l1.destroy()
        amount_entry.destroy()
        b13.destroy()
        b14.destroy()
        account_menu()

    b14 = Button(root, text="BACK", width="25", command=back)
    b14.pack()


#Handling deposit_in_account()
def handling_deposit():
    try:
        amount = int(amount_entry.get())
        user_account.deposit_amount(amount)
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a valid integer.")


#change pin menu
def change_pin_menu():

    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()

    l1 = Label(root, text="old pin")
    l1.pack()

    global e2,e3
    e2 = Entry(root, width=25)
    e2.pack()

    l2 = Label(root, text="new pin")
    l2.pack()

    e3 = Entry(root, width=25)
    e3.pack()

    b15 = Button(root, text="CHANGE", width=25, command=handling_set_pin)
    b15.pack()

    def back():
        l1.destroy()
        e2.destroy()
        l2.destroy()
        e3.destroy()
        b15.destroy()
        b16.destroy()
        account_menu()

    b16 = Button(root, text="BACK", width="25", command=back)
    b16.pack()


#handling set_pin()
def handling_set_pin():

    try:
        old_pin = int(e2.get())
        new_pin = int(e3.get())
        user_account.set_pin(old_pin, new_pin)

    except:
        messagebox.showinfo("ERROR", "Enter correct values")

#savings menu
def savings_menu():
    b1.destroy()
    b2.destroy()
    b3.destroy()

    global b7, b8, b9
    b7 = Button(root, text="DEPOSIT IN SAVINGS", width=25, command=savings_deposit)
    b7.pack()

    b8 = Button(root, text="SEE INFO", width=25, command=savings.get_details)
    b8.pack()

    def back():
        b7.destroy()
        b8.destroy()
        b9.destroy()
        main()

    b9 = Button(root, text="Back",command=back, width=25)
    b9.pack()


#savings deposit menu
def savings_deposit():

    b7.destroy()
    b8.destroy()
    b9.destroy()

    l1 = Label(root, text="AMOUNT")
    l1.pack()

    global deposit_entry
    deposit_entry = Entry(root)
    deposit_entry.pack()

    b18 = Button(root, text="DEPOSIT", width=25, command=handling_savings_deposit)
    b18.pack()

    def back():

        l1.destroy()
        deposit_entry.destroy()
        b18.destroy()
        b17.destroy()
        savings_menu()

    b17 = Button(root, text="Back",command=back, width=25)
    b17.pack()

#handling savings deposit
def handling_savings_deposit():

    try:
        amount = int(deposit_entry.get())
        savings.deposit_amount(amount)

    except:
        messagebox.showinfo("ERROR", "Try entering valid amount")


#expense menu
def expense_menu():
    b1.destroy()
    b2.destroy()
    b3.destroy()

    global b9,b10,b11,b12
    b9 = Button(root, text="ADD EXPENSE", width=25, command=add_expense_menu)
    b9.pack()

    b10 = Button(root, text="REMOVE EXPENSE", width=25, command=delete_expense_menu)
    b10.pack()

    b11 = Button(root, text="DISPLAY EXPENSE", width=25, command=dispaly_expense_menu)
    b11.pack()

    def back():
        b9.destroy()
        b10.destroy()
        b11.destroy()
        b12.destroy()
        main()

    b12 = Button(root, text="Back",command=back, width=25)
    b12.pack()


#add expense menu
def add_expense_menu():
    b9.destroy()
    b10.destroy()
    b11.destroy()
    b12.destroy()

    global var
    var = StringVar(value="Food")

    food = Radiobutton(root, text="Food", variable=var, value="Food")
    food.pack()
    rent = Radiobutton(root, text="rent", variable=var, value="Rent")
    rent.pack()
    bill = Radiobutton(root, text="Bill", variable=var, value="Bill")
    bill.pack()
    clothing = Radiobutton(root, text="Clothing", variable=var, value="clothing")
    clothing.pack()
    grocery = Radiobutton(root, text="Grocery Item", variable=var, value="Grocery Item")
    grocery.pack()
    miscellaneous = Radiobutton(root, text="Miscellaneous", variable=var, value="Miscellaneous")
    miscellaneous.pack()

    global name_entry, date_entry, amount_entry
    l1 = Label(root, text="NAME")
    l1.pack()

    name_entry = Entry(root, width=25)
    name_entry.pack()

    l2 = Label(root, text="DATE")
    l2.pack()

    date_entry = Entry(root, width=25)
    date_entry.pack()

    l3 = Label(root, text="AMOUNT")
    l3.pack()

    amount_entry = Entry(root, width=25)
    amount_entry.pack()

    b19 = Button(root, text="ADD", width=25, command=adding_expense)
    b19.pack()

    def back():
        food.destroy()
        rent.destroy()
        bill.destroy()
        clothing.destroy()
        grocery.destroy()
        miscellaneous.destroy()
        l1.destroy()
        name_entry.destroy()
        l2.destroy()
        date_entry.destroy()
        l3.destroy()
        amount_entry.destroy()
        b19.destroy()
        b20.destroy()
        expense_menu()

    b20 = Button(root, text="Back",command=back, width=25,)
    b20.pack()


#handling add_expense()
def adding_expense():

    name = name_entry.get()
    date = date_entry.get()
    amount = int(amount_entry.get())
    category = var.get()

    if name == "" or date == "" or amount == "":
        messagebox.showinfo("ERROR", "Entry cannot be empty")
        return

    else:
        expense.get_name(name)
        expense.get_date(date)
        expense.get_category(category)
        expense.get_amount(amount)
        expense.save_to_database()
        messagebox.showinfo("SUCCESS","Expense successfully added!")

#deleting expense
def delete_expense_menu():
    b9.destroy()
    b10.destroy()
    b11.destroy()
    b12.destroy()

    l1 = Label(root, text="Expense ID")
    l1.pack()

    global id_entry
    id_entry = Entry(root, width=25)
    id_entry.pack()

    b21 = Button(root, text="DELETE", width=25, command=deleting_expense)
    b21.pack()

    def back():
        l1.destroy()
        id_entry.destroy()
        b21.destroy()
        b22.destroy()
        expense_menu()

    b22 = Button(root, text="Back",command=back, width=25)
    b22.pack()

#handling delete_expense()
def deleting_expense():

    expense_id = int(id_entry.get())

    if expense_id <= 0:
        messagebox.showerror("ERROR","invalid expense id")
        return

    else:
        expense.delete_expense(expense_id)
        messagebox.showinfo("SUCCESS","Expense successfully deleted")

def dispaly_expense_menu():
    b9.destroy()
    b10.destroy()
    b11.destroy()
    b12.destroy()

    list = Listbox(root)
    list.pack()

    def back():
        list.destroy()
        b23.destroy()
        expense_menu()

    b23 = Button(root, text="Back",command=back, width=25)
    b23.pack()


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
