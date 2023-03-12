import tkinter as tk

#기본 window 만들기
window = tk.Tk()

window.title('My First GUI Program')
window.resizable(True, False)

width = 500
height = 400
x = 100
y = 100
window.geometry('{}x{}+{}+{}'.format(width, height, x,y))

'''================================================================================================================'''
#widget(e.g. button, textbox)
#user 가 상호작용하는 인터페이스 요소

 #1번 widget
label = tk.Label(    
    window,
    text = 'Coding is fun',
    font = ('Connsolas', 30),
    fg = 'yellow',
    bg = 'black',
    width = 6,
    height = 5
)
label.pack() #label 을 window 에 locate
'''================================================================================================================'''
button_click_cnt = 0
def event_fn():
    global button_click_cnt
    button_click_cnt += 1
    label.config(text=str(button_click_cnt))
    if button_click_cnt %2 == 0:

        label.config(bg='red')
    else:
        label.config(bg='black')

button = tk.Button()

button = tk.Button(
    window, 
    text = 'Button this is',
    width = 20,
    height = 2,
    command = event_fn
)
button.pack()

'''================================================================================================================'''
#entry 사용자로부터 text 입력받는다

def entry_event_fn(user_input):
    label.config(text='{}'.format(entry.get()))

entry = tk.Entry(window)
entry.bind('<Return>', entry_event_fn)
entry.pack()
'''================================================================================================================'''
#menu: 자주 사용하는 기능 선택

def close():
    window.quit()
    window.destroy()

menubar = tk.Menu(window)

menu_1 = tk.Menu(menubar, tearoff=False)
menu_1.add_command(label = 'Open', command=close)
menu_1.add_command(label = 'Open Folder')
menu_1.add_command(label = 'Open Directory')

menu_2 = tk.Menu(menubar, tearoff=False)
menu_2.add_command(label = 'Undo')
menu_2.add_command(label='Redo')
menu_2.add_separator()
menu_2.add_command(label='Cut')

menubar.add_cascade(label='File', menu=menu_1)
menubar.add_cascade(label='Edit', menu=menu_2)

window.config(menu=menubar)

window.mainloop()