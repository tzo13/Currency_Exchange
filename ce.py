from tkinter import *
from tkinter.ttk import  *
from ttkthemes import ThemedTk
import requests, json



win = ThemedTk(theme = "equilux")
win.configure(themebg = "equilux")
win.title("currency exchange")
win.resizable(height=False, width=False)

def c():
    makis ="K3MQO5ISZGAYC6NI"
    base = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    eurl = base + "&from_currency=" + a2.get() + "&to_currency=" + a3.get() + "&apikey=" + makis
    print(eurl)

    robj = requests.get(eurl)
    result =robj.json()

    rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    print(rate)


    oeo = float(a1.get())
    mpla = oeo * rate
    print (mpla)
    c.configure(text = mpla)



a = Label(win, text = "Amount")
f = Label(win, text = "From")
t = Label(win, text = "To")

a1 = Entry(win)
a2 = Combobox(win, state="readonly")
a3 = Combobox(win, state="readonly")
a4 = Button(win, text = "Convert",command=c)
c = Label(win)


a2['values']=('EUR','USD','GBP')
a3['values']=('EUR','USD','GBP')


a.grid(row = 0 , column = 0)
f.grid(row = 0 , column = 1)
t.grid(row = 0 , column = 2)
a1.grid(row = 1 , column = 0)
a2.grid(row = 1 , column = 1)
a3.grid(row = 1 , column = 2)
a4.grid(row = 1 , column = 3)
c.grid(row = 2,column = 0)


win.mainloop()