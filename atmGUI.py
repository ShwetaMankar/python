from tkinter import*
import time

#creating window
root = Tk()
root.geometry("900x550") #default size in which window will open
root.title("ATM Machine")#window title
root.configure(bg="silver")#window background color

tops = Frame(root, bg="white", width=1000, height=50, relief=SUNKEN)
tops.pack(side=TOP)

f1 = Frame(root, bg="white", width=400, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, bg="chartreuse3", width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

#store local time in localtime
localtime = time.asctime(time.localtime(time.time()))

#ATM Machine Label
lblinfo = Label(tops, font=('aria', 30, 'bold'), text="ATM Machine", fg="Black", bg='limegreen', padx=17, pady=0, bd=10, anchor='w')
lblinfo.grid(row=0, column=0)

#current time on ATM GUI
lblinfo = Label(tops, font=('aria', 20, ), text=localtime, fg="crimson", bg="silver", anchor='w')
lblinfo.grid(row=1, column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
acca = " "

#bank account credentials
def bank():
    global acca
    accno = ["0009879", "0001234", "0009829", "1002789", "2030456"]
    account = number.get()
    if account in accno:
        label.config(text="Registered member")   #check if number is registered
        bank = {"0009879": 10000, "0001234": 20000, "0009829": 30000}
        balance = bank[account]
        acca = balance

    else:
        label.config(text="Non-registered member")   #check if number is registered

#enter deposite amount in account
def deposit():
    global acca
    amo = float(amount.get())
    balen = acca+amo
    label3.config(text=("Net Balance:", str(balen))) #show balane after deposited amount

#withdraw amount from your account
def withdraw():
    global acca
    wd = float(withd.get())
    if acca >= wd:
        ace = acca-wd
        label4.config(text=("Net Balance: ", str(ace))) #show balane after withdrawal amount
    else:
        label4.config(text=("Insufficient Balance")) #show insufficient balance if it is

#to check balance
def bal():
    global acca
    label.config(text=("Net balance: ", str(acca)))

#to reset all fields entered on gui
def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")
        

#label to show - 'Enter the account number'
lbl = Label(f1, font=('aria',16,'bold'), text="Enter the account number:   ", bg="white", fg="black", bd=10, anchor='w')
lbl.grid(row=0, column=3)
txt = Entry(f1, font = ('arial', 16, 'bold'), textvariable=number, bd=6, insertwidth=4, bg="cornflowerblue", justify='right')
txt.grid(row=0, column=4)
label = Label(f1, fg="black", bg="white", font=('aria', 16, 'bold'))
label.grid(row=1, column=4)

#button to submit enterd account number to do further process and will show if registred or not
btnsubmit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="SUBMIT", bg="cornflowerblue", command=bank)
btnsubmit.grid(row=0, column=4)

lblTotal = Label(f1, text="                                            ", fg="black", bg="white",)
lblTotal.grid(row=3, columnspan=10)

#label to show - 'Enter the amount to be deposited'
lbl = Label(f1, font=("aria", 16, 'bold'), text="Enter the amount to deposit: ", fg="black", bg="white", bd=10, anchor='w')
lbl.grid(row=4, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=amount, bd=6, insertwidth=4, bg="cornflowerblue", justify='right')
txt.grid(row=4, column=4)

#label to show balance after deposited amount
label3 = Label(f1, fg="black", bg="white",font=('aria', 16, 'bold'))
label3.grid(row=5, column=4)

#button to deposite entered amount
btndeposite = Button(f2, padx=16, pady=4, bd=10, fg='black', font=('arial', 16, 'bold'), width=7, text="DEPOSIT", bg="cornflowerblue", command=deposit)
btndeposite.grid(row=4, column=4)

lblTotal = Label(f1, text="                                            ", fg="black", bg="white")
lblTotal.grid(row=7, columnspan=10)

#label to show - 'Enter the amount to be withdrawn'
lbl = Label(f1, font=("aria", 16, 'bold'), text="Enter the amount to withdraw: ", fg="black", bg="white", bd=10, anchor='w')
lbl.grid(row=8, column=3)

txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=withd, bd=6, insertwidth=4, bg="cornflowerblue", justify='right')
txt.grid(row=8, column=4)

label5 = Label(f1, fg="black", bg="white", font=('aria', 16, 'bold'))
label5.grid(row=10, column=4)

label4 = Label(f1, fg="black", bg="white", font=('aria', 16, 'bold'))
label4.grid(row=9, column=4)

#button to withdraw entered amount
btnwithdraw = Button(f2, padx=16, pady=4, bd=10, fg="black", font=("arial", 16, 'bold'), width=7, text="WITHDRAW", bg="cornflowerblue", command=withdraw)
btnwithdraw.grid(row=8, column=4)

#button to check balance
btnbal = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('arial', 16, 'bold'), width=7, text="BALANCE", bg="cornflowerblue", command=bal)
btnbal.grid(row=10, column=4)

#button to reset all fields
btnrest = Button(f2, padx=16, pady=4, bd=10, fg="black", font=("arial", 16, 'bold'), width=7, text="RESET", bg="cornflowerblue", command=reset)
btnrest.grid(row=11, column=4)

#button to exit from atm
btnexit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('arial', 16, 'bold'), width=7, text="EXIT", bg="cornflowerblue", command=root.destroy)
btnexit.grid(row=12, column=4)


#Runs the window till it is closed manually
root.mainloop()
