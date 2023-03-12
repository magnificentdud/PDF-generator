from currency import get_currency_ratio

import tkinter as tk

#기본 window 만들기
window = tk.Tk()

window.title('My First GUI Program')
window.resizable(True, False)

label = tk.Label(window, text = '대기중', height = 4)
label.pack()


window.title('MyfirstGUI')
window.geometry('{}x{}+{}+{}'.format(500,400,100,100))


#get input from user, a number
#calculate currency value and display
def entry_event_fn(user_input):
    currency_s = {'USD':'$', 'EUR': '€', 'JPY': '¥'}
    curr = get_currency_ratio(currency)
    result = float(entry.get()) * curr
    label.config(text='{}{}'.format(currency_s[currency],result))




entry = tk.Entry(window)
entry.bind('<Return>', entry_event_fn)
entry.pack()

def click():
    global currency
    currency = tk_currency.get()


# bringiing currency value from the internet
# code ibrary from currencey.py
tk_currency = tk.StringVar(value = None)
currency = None
radio_btn1 = tk.Radiobutton(
        window, text = 'USD', value = 'USD', variable = tk_currency, command=click)
radio_btn2 = tk.Radiobutton(
        window, text = 'EUR', value = 'EUR', variable = tk_currency, command=click)
radio_btn3 = tk.Radiobutton(
        window, text = 'JPY', value = 'JPY', variable = tk_currency, command=click)
        
        
radio_btn1.pack()
radio_btn2.pack()
radio_btn3.pack()

# need this code 
#set up actual window
window.mainloop()