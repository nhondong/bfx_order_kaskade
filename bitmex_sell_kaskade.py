import config
import ccxt
import sys
from tkinter import *
import tkinter.ttk as ttk

pair = "BTC/USD"
side = ""
amount = 0
price_level = 0
price_range = 0
ordercount = 0
type = "Limit"

####################################
# Einstellungen für die Kaskade    #
####################################

def quit_window():
    global side
    global price_level
    global amount
    global price_range
    global ordercount
    global type

    price_level = int(e1.get())
    amount = int(e2.get())
    price_range = int(e3.get())
    ordercount = int(e4.get())
    side = R1.getvar(var)
    type = cb.get()
    master.destroy()

master = Tk()
master.title("Welche Order möchtest du einstellen?")
master.resizable(width=False, height=False)
master.geometry('500x400')
Label(master, text="Side:").grid(row=0)
Label(master, text="Type:").grid(row=1)
Label(master, text="Preis:").grid(row=2)
Label(master, text="Ordergröße:").grid(row=3)
Label(master, text="Range:").grid(row=4)
Label(master, text="Anzahl Orders:").grid(row=5)

var = ""
R1 = Radiobutton(master, text="Long", variable=var, value="buy")
R2 = Radiobutton(master, text="Short", variable=var, value="sell")


cb = ttk.Combobox(master, values=("Limit", "StopLimit", "Market", "Stop"))
cb.set("Limit")

# Limit, StopLimit or 'Market', or 'Stop' or 'StopLimit'

e1 = Entry(master)
e1.insert(END, '4500')
e2 = Entry(master)
e2.insert(END, '500')
e3 = Entry(master)
e3.insert(END, '40')
e4 = Entry(master)
e4.insert(END, '10')

R1.grid(row=0, column=1)
R2.grid(row=0, column=2)
cb.grid(row=1, column=1)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)
e4.grid(row=5, column=1)


Button(master, text='Positionen einstellen', command=quit_window).grid(row=7, column=0, sticky=W, pady=4)
master.mainloop()

def closeEvent(self, event):
    # code to be executed
    print("lets go")

if amount >= 0:
    ####################################
    #  Orders werden eingestellt       #
    ####################################

    exchange = ccxt.bitmex({
        'apiKey': config.bitmex_order_apikey,
        'secret': config.bitmex_order_secret,
        'enableRateLimit': True,
    })

    # extra params and overrides
    params = {
    #    'stopPx': 6000.0,  # if needed
     }

    pos_amount=amount/ordercount
    price_low = price_level - price_range/2
    price_steps = price_range / ordercount

    for i in range(0,ordercount -1):
        #Preis berechnen
        pos_price = round(price_low + i*price_steps,0)
        try:
            order = exchange.create_order(pair, type, side, pos_amount, pos_price, params)
            # print(order)
        except:
            print(sys.exc_info()[1])
            break