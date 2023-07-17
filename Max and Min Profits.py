from tkinter import *

root=Tk()
root.title("Profits")
root.geometry("500x500")
root.configure(background="light blue")

month = ("January", "February", "March", "April", "May", 
         "June", "July", "August", "September", "October", 
         "November", "December")

profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000,
           54000, 10000, 30000, 70000, 90000)

label1 = Label(root, text="")
label1.place(relx=0.4, rely=0.4)

label2 = Label(root, text="")
label2.place(relx=0.1, rely=0.5)

label3 = Label(root, text="")
label3.place(relx=0.4, rely=0.6)

label4 = Label(root, text="")
label4.place(relx=0.1, rely=0.7)

def maxs():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    label1["text"] = max_profit_index
    max_profit_month = month[max_profit_index]
    label2["text"] = "The maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month)

def mins():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    label3["text"] = min_profit_index 
    min_profit_month = month[min_profit_index]
    label4["text"] = "The minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month)

btn1 = Button(root, text="Show Max Profit: ", command = maxs)
btn1.place(relx= 0.4,rely = 0.3,)

btn2 = Button(root, text="Show Min Profit: ", command = mins)
btn2.place(relx= 0.4,rely = 0.2,)

root.mainloop()