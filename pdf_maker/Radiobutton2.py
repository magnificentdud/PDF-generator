import tkinter as tk
window = tk.Tk()
window.title('MyFirst GUI')

window.geometry('300x300+100+100')
window.resizable(False, False)

def flash():
    checkbutton1.flash() #flash button
    checkbutton2.flash()

def set_label():
    value1 = check_button1_value.get() # convert tk variable into python variable
    value2 = check_button2_value.get()
    label1.config(text=str(value1))
    label2.config(text=str(value2))

check_button1_value = tk.BooleanVar() # tkinter variable ()
check_button2_value = tk.BooleanVar()

label1  = tk.Label(window, text = str(check_button1_value.get())) #label object
label2 = tk.Label(window, text = str(check_button2_value.get()))

label1.pack()
label2.pack()

checkbutton1 = tk.Checkbutton( # checkbutton object
    window, text='O',
    variable = check_button1_value, #bind tk variable to checkbutton object
    activebackground = 'blue', # temporarily switch background color to blue when clicked
    command = set_label

)

checkbutton2 = tk.Checkbutton(
    window, text='△', variable=check_button2_value,
    command=flash
)

checkbutton1.pack()
checkbutton2.pack()

window.mainloop()
