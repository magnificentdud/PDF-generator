import tkinter as tk
window = tk.Tk()
window.title('MyFirst GUI')

window.geometry('300x300+100+100')
window.resizable(False, False)

def check():
    value = radio_button_val.get() #convert tk variable into python variable
    label.config(text='Value:'+str(value))

radio_button_val = tk.IntVar() #tk variable
value = radio_button_val.get() #convert tk variable into python processible variable

label=tk.Label(window, text='Value:'+str(value)) #label object
label.pack()

radio1=tk.Radiobutton(
    window, text = '1번',
    value = 10,
    variable = radio_button_val,
    command = check
)

radio2 = tk.Radiobutton(window, text = '2번', value = 20, variable = radio_button_val, command=check)
radio3 = tk.Radiobutton(window, text = '3번', value = 30, variable = radio_button_val, command=check)

radio1.pack()
radio2.pack()
radio3.pack()
window.mainloop()