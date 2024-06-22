from main import *
from tkinter import *
from tkinter import ttk

root = Tk()

user_account.retrieve()
savings.retrieve()

root.title("personalfinance tracker")
root.geometry("700x600")
root.config(bg="steel blue")

#main label
label = Label(root, text="PERSONAL FINANCE TRACKER", font="Calibri 30 bold")
label.pack(pady=20, fill=X)
label.config(fg="white", bg="light blue")


#accounts menu
def account_menu():

    f1.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    exit.destroy()

    global f2, b4, b5, b6, b7
    f2 = Frame(root, bg="steel blue")
    f2.pack(expand=TRUE, anchor=CENTER)

    b4 = Button(f2, text="DEPOSIT MONEY", width=25, height=2, bg="light grey", command=deposit_menu)
    b4.pack(padx=3, pady=3)

    b5 = Button(f2, text="WITHDRAW", width=25,height=2, bg="light grey", command=withdraw_menu)
    b5.pack(padx=3, pady=3)

    b24 = Button(f2, text="TRANSACTION HISTORY", width=25,height=2, bg="light grey", command=displaying_transactions)
    b24.pack(padx=3, pady=3)

    b6 = Button(f2, text="CHECK DETAILS", width=25,height=2, bg="light grey", command=user_account.get_details)
    b6.pack(padx=3, pady=3)

    def back():
        f2.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b7.destroy()
        main()

    b7 = Button(root, text="BACK", width=15, height=1, bg="light grey", command=back)
    b7.pack(padx=20, pady=20, side=BOTTOM)

# deposit menu
def deposit_menu():

    f2.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()

    global amount_entry, date_entry, f3
    f3 = Frame(root, bg="steel blue")
    f3.pack(expand=TRUE, anchor=CENTER)

    l2 = Label(f3, text="DATE", bg="steel blue")
    l2.pack(padx=3, pady=3)

    date_entry = Entry(f3, width=25)
    date_entry.pack(padx=3, pady=3)

    l1 = Label(f3, text="AMOUNT", bg="steel blue")
    l1.pack(padx=3, pady=3)

    amount_entry= Entry(f3, width=25)
    amount_entry.pack(padx=3, pady=3)

    b13 = Button(f3, text="DEPOSIT", width=15, height=1 , bg="light grey", command=handling_deposit)
    b13.pack(padx=20, pady=20)

    def back():
        f3.destroy()
        l1.destroy()
        l2.destroy()
        amount_entry.destroy()
        date_entry.destroy()
        b13.destroy()
        b14.destroy()
        account_menu()

    b14 = Button(root, text="BACK", width=15, height=1, bg="light grey",command=back)
    b14.pack(padx=20, pady=20, side=BOTTOM)


#Handling deposit_in_account()
def handling_deposit():
    try:
        amount = int(amount_entry.get())
        date = date_entry.get()
        user_account.deposit_amount(amount, date)
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a valid amount")


#withdra menu
def withdraw_menu():

    f2.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()

    global f1,pin_e, date_e, amount_e
    f4 = Frame(root, bg="steel blue")
    f4.pack(expand=TRUE, anchor=CENTER)

    l3 = Label(f4, text="PIN", bg="steel blue")
    l3.pack(padx=1, pady=1)

    pin_e = Entry(f4, width=25)
    pin_e.pack(padx=1, pady=1)

    l1 = Label(f4, text="DATE", bg="steel blue")
    l1.pack(padx=1, pady=1)

    date_e = Entry(f4, width=25)
    date_e.pack(padx=1, pady=1)

    l2 = Label(f4, text="AMOUNT", bg="steel blue")
    l2.pack(padx=1, pady=1)

    amount_e = Entry(f4, width=25)
    amount_e.pack(padx=1, pady=1)

    b15 = Button(f4, text="WITHDRAW", width=15, height=1, command=handling_withdraw)
    b15.pack(padx=20, pady=20)

    def back():
        f4.destroy()
        l1.destroy()
        pin_e.destroy()
        l2.destroy()
        date_e.destroy()
        l3.destroy()
        amount_e.destroy()
        b15.destroy()
        b16.destroy()
        account_menu()

    b16 = Button(root, text="BACK", width=15,bg="light grey", command=back)
    b16.pack(padx=20, pady=20)


#handling set_pin()
def handling_withdraw():
    try:
        amount = int(amount_e.get())
        date = date_e.get()
        pin = int(pin_e.get())
        user_account.withdraw(amount, date, pin)

    except:
        messagebox.showerror("ERROR","invalid entry")

#dispaying transaction history in a treeview
def displaying_transactions():

    f2.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()

    tree = ttk.Treeview(root)
    tree["columns"] = ("Date", "Deposit", "Withdraw", "Amount")

    tree.column("#0", width=0)
    tree.column("Date", anchor=W, width=120)
    tree.column("Deposit", anchor=W, width=120)
    tree.column("Withdraw", anchor=W, width=120)
    tree.column("Amount", anchor=W, width=120)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Date", text="Date", anchor=W)
    tree.heading("Deposit", text="Deposit", anchor=W)
    tree.heading("Withdraw", text="Withdraw", anchor=W)
    tree.heading("Amount", text="Amount", anchor=W)

    with open("balance.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert(parent="", index=END, values=row)

    scrollbar = Scrollbar(tree, command=tree.yview)
    tree.config(yscrollcommand=scrollbar.set)

    scrollbar.pack(padx=10, pady=10, side=RIGHT, fill=Y)
    tree.pack(padx=10, pady=10, expand=TRUE, fill=BOTH)

    def back():

        tree.destroy()
        b25.destroy()
        account_menu()

    b25 = Button(root, text="BACK", width=15,bg="light grey", command=back)
    b25.pack(padx=20, pady=20)

#savings menu
def savings_menu():

    exit.destroy()
    f1.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()

    global f5,b7, b8, b9
    f5 = Frame(root,bg="steel blue")
    f5.pack(expand=TRUE, anchor=CENTER)

    b7 = Button(f5, text="DEPOSIT IN SAVINGS", bg="light grey",width=25,height=2, command=savings_deposit)
    b7.pack(padx=3, pady=3)

    b10 = Button(f5, text="TRANSACTION HISTORY", bg="light grey",width=25,height=2, command=saving_transaction)
    b10.pack(padx=3, pady=3)

    b8 = Button(f5, text="SEE INFO", bg="light grey", width=25,height=2, command=savings.get_details)
    b8.pack(padx=3, pady=3)

    def back():
        f5.destroy()
        b7.destroy()
        b8.destroy()
        b9.destroy()
        b10.destroy()
        main()

    b9 = Button(root, text="BACK", bg="light grey", command=back, width=15)
    b9.pack(padx=20, pady=20)


#savings deposit menu
def savings_deposit():
    f5.destroy()
    b7.destroy()
    b8.destroy()
    b9.destroy()

    global f6,deposit_entry,saving_date
    f6 = Frame(root, bg="steel blue")
    f6.pack(expand=TRUE, anchor=CENTER)

    l1 = Label(f6, text="DATE", bg="steel blue")
    l1.pack(padx=3, pady=3)

    saving_date = Entry(f6, width=25)
    saving_date.pack(padx=3, pady=3)

    l2 = Label(f6, text="AMOUNT", bg="steel blue")
    l2.pack(padx=3, pady=3)

    deposit_entry = Entry(f6, width=25)
    deposit_entry.pack(padx=3, pady=3)

    b18 = Button(f6, text="DEPOSIT", bg="light grey", width=15, height=1, command=handling_savings_deposit)
    b18.pack(padx=20, pady=20)

    def back():

        f6.destroy()
        l1.destroy()
        l2.destroy()
        deposit_entry.destroy()
        saving_date.destroy()
        b18.destroy()
        b17.destroy()
        savings_menu()

    b17 = Button(root, text="BACK", bg="light grey", command=back, width=15)
    b17.pack(padx=20, pady=20)


#handling savings deposit
def handling_savings_deposit():

    try:
        amount = int(deposit_entry.get())
        date = saving_date.get()
        savings.deposit_amount(amount, date)

    except:
        messagebox.showinfo("ERROR", "Try entering valid amount")


#displaying savings transaction history
def saving_transaction():

    f5.destroy()
    b7.destroy()
    b8.destroy()
    b9.destroy()

    tree = ttk.Treeview(root)
    tree["columns"] = ("Date", "Deposit", "Amount")

    tree.column("#0", width=0)
    tree.column("Date", anchor=W, width=120)
    tree.column("Deposit", anchor=W, width=120)
    tree.column("Amount", anchor=W, width=120)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Date", text="Date", anchor=W)
    tree.heading("Deposit", text="Deposit", anchor=W)
    tree.heading("Amount", text="Amount", anchor=W)

    with open("Savings_deposit.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert(parent="", index=END, values=row)

    scrollbar = Scrollbar(tree, command=tree.yview)
    tree.config(yscrollcommand=scrollbar.set)

    scrollbar.pack(padx=10, pady=10, side=RIGHT, fill=Y)
    tree.pack(padx=10, pady=10, expand=TRUE, fill=BOTH)

    def back():

        tree.destroy()
        b26.destroy()
        savings_menu()

    b26 = Button(root, text="BACK", width=15,bg="light grey", command=back)
    b26.pack(padx=20, pady=20)


#expense menu
def expense_menu():
    f1.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    exit.destroy()

    global f7,b9,b10,b11,b12
    f7 = Frame(root,bg="steel blue")
    f7.pack(expand=TRUE, anchor=CENTER)

    b9 = Button(f7, text="ADD EXPENSE", width=25, bg="light grey", height=2, command=add_expense_menu)
    b9.pack(padx=3, pady=3)

    b10 = Button(f7, text="REMOVE EXPENSE", width=25, bg="light grey", height=2, command=delete_expense_menu)
    b10.pack(padx=3, pady=3)

    b11 = Button(f7, text="DISPLAY EXPENSE", width=25, bg="light grey", height=2, command=dispaly_expense_menu)
    b11.pack(padx=3, pady=3)

    def back():

        f7.destroy()
        b9.destroy()
        b10.destroy()
        b11.destroy()
        b12.destroy()
        main()

    b12 = Button(root, text="BACK",command=back, bg="light grey", width=15)
    b12.pack(padx=20, pady=20)


#add expense menu
def add_expense_menu():
    f7.destroy()
    b9.destroy()
    b10.destroy()
    b11.destroy()
    b12.destroy()

    global f8,var
    f8 = Frame(root, bg="steel blue")
    f8.pack(expand=TRUE, anchor=CENTER)
    var = StringVar(value="Food")

    food = Radiobutton(f8, text="Food", bg="steel blue", variable=var, value="Food")
    food.pack(padx=10, anchor=W)
    rent = Radiobutton(f8, text="rent", bg="steel blue", variable=var, value="Rent")
    rent.pack(padx=10, anchor=W)
    bill = Radiobutton(f8, text="Bill", bg="steel blue", variable=var, value="Bill")
    bill.pack(padx=10, anchor=W)
    clothing = Radiobutton(f8, text="Clothing", bg="steel blue", variable=var, value="clothing")
    clothing.pack(padx=10, anchor=W)
    travel = Radiobutton(f8, text="Travel", bg="steel blue", variable=var, value="clothing")
    travel.pack(padx=10, anchor=W)
    grocery = Radiobutton(f8, text="Grocery Item", bg="steel blue", variable=var, value="Grocery Item")
    grocery.pack(padx=10, anchor=W)
    others = Radiobutton(f8, text="Others", bg="steel blue", variable=var, value="Miscellaneous")
    others.pack(padx=10, anchor=W)

    global name_entry, date_entry, amount_entry
    l1 = Label(f8, text="NAME", bg="steel blue")
    l1.pack(padx=1, pady=1)

    name_entry = Entry(f8, width=25)
    name_entry.pack(padx=1, pady=1)

    l2 = Label(f8, text="DATE", bg="steel blue")
    l2.pack(padx=1, pady=1)

    date_entry = Entry(f8, width=25)
    date_entry.pack(padx=1, pady=1)

    l3 = Label(f8, text="AMOUNT", bg="steel blue")
    l3.pack(padx=1, pady=1)

    amount_entry = Entry(f8, width=25)
    amount_entry.pack(padx=1, pady=1)

    b19 = Button(f8, text="ADD", width=15, bg="light grey", command=adding_expense)
    b19.pack(padx=20, pady=20)

    def back():
        f8.destroy()
        food.destroy()
        rent.destroy()
        bill.destroy()
        clothing.destroy()
        grocery.destroy()
        others.destroy()
        l1.destroy()
        name_entry.destroy()
        l2.destroy()
        date_entry.destroy()
        l3.destroy()
        amount_entry.destroy()
        b19.destroy()
        b20.destroy()
        expense_menu()

    b20 = Button(root, text="BACK", bg="Light grey",command=back, width=15,)
    b20.pack(padx=20, pady=20)


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

    f7.destroy()
    b10.destroy()
    b11.destroy()
    b12.destroy()

    global id_entry,f9

    f9 = Frame(root, bg="steel blue")
    f9.pack(expand=TRUE, anchor=CENTER)

    l1 = Label(f9, text="Expense ID", bg="steel blue")
    l1.pack(padx=3, pady=3)

    id_entry = Entry(f9, width=25)
    id_entry.pack(padx=3, pady=3)

    b21 = Button(f9, text="DELETE", width=15, bg="light grey", command=deleting_expense)
    b21.pack(padx=20, pady=20)

    def back():
        f9.destroy()
        l1.destroy()
        id_entry.destroy()
        b21.destroy()
        b22.destroy()
        expense_menu()

    b22 = Button(root, text="BACK", bg="light grey", command=back, width=15)
    b22.pack(padx=20, pady=20)

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

    f7.destroy()
    b10.destroy()
    b11.destroy()
    b12.destroy()

    global tree
    tree = ttk.Treeview(root)

    tree["columns"] = (["ID", "NAME", "CATEGORY", "DATE", "AMOUNT"])

    tree.column("#0", width=0)
    tree.column("ID", width=50, anchor=W)
    tree.column("NAME", width=120, anchor=W)
    tree.column("CATEGORY", width=120, anchor=W)
    tree.column("DATE", width=120, anchor=W)
    tree.column("AMOUNT", width=120, anchor=W)

    tree.heading("#0", text="")
    tree.heading("ID", text="ID", anchor=W)
    tree.heading("NAME", text="NAME", anchor=W)
    tree.heading("CATEGORY", text="CATEGORY", anchor=W)
    tree.heading("DATE", text="DATE", anchor=W)
    tree.heading("AMOUNT", text="AMOUNT", anchor=W)

    scrollbar = Scrollbar(tree, command=tree.yview)
    tree.config(yscrollcommand=scrollbar.set)

    scrollbar.pack(padx=10, pady=10, side=RIGHT, fill=Y)
    tree.pack(padx=10, pady=10, expand=TRUE, fill=BOTH)

    display_expenses()

    def back():

        tree.destroy()
        b23.destroy()
        expense_menu()

    b23 = Button(root, text="BACK", bg="light grey", command=back, width=15)
    b23.pack(padx=20, pady=20)


#handling expense
def display_expenses():

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
        tree.insert(parent="", index=END, values=record)

    mydb.close()

#main menu
def main():

    global f1,b1,b2,b3, exit
    f1 = Frame(root, bg="steel blue")
    f1.pack(expand=TRUE, anchor=CENTER)

    b1 = Button(f1, text="ACCOUNT", width=25, height=2, bg="light grey", command=account_menu)
    b1.pack(padx=3, pady=3)
    b2 = Button(f1, text="SAVINGS", width=25, height=2, bg="light grey", command=savings_menu)
    b2.pack(padx=3, pady=3)
    b3 = Button(f1, text="EXPENSE", width=25, height=2, bg="light grey", command=expense_menu)
    b3.pack(padx=3, pady=3)

    exit = Button(root, text="EXIT", width=15, height=1, bg="light grey", command=root.destroy)
    exit.pack(padx=20, pady=20)

f1 = Frame(root, bg="steel blue")
f1.pack(expand=TRUE, anchor=CENTER)

b1 = Button(f1, text="ACCOUNT", width=25, height=2, bg="light grey", command=account_menu)
b1.pack(padx=3,pady=3)
b2 = Button(f1, text="SAVINGS", width=25, height=2, bg="light grey", command=savings_menu)
b2.pack(padx=3,pady=3)
b3 = Button(f1, text="EXPENSE", width=25, height=2, bg="light grey", command=expense_menu)
b3.pack(padx=3,pady=3)

exit = Button(root, text="EXIT", width=15, height=1, bg="light grey", command=root.destroy)
exit.pack(padx=20, pady=20)

#making taskbar
text = StringVar()
text.set("group project\t\t\tDeveloped by Hamza and Sunnan\t\t\t56804,56754")
bar = Label(root, textvariable= text)
bar.config(fg="black", bg="light blue", height=2)
bar.pack(side=BOTTOM, fill=X)

root.mainloop()
