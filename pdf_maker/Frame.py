import tkinter as tk

window = tk.Tk()
window.title("My Firgt GUI")
window.resizable(True,True)

width = 500
height = 400
x = 100
y = 100
window.geometry('{}x{}+{}+{}'.format(width, height, x,y))

frame1 = tk.Frame(
    window,             #frame object 생성
    relief="groove",    #border 모양 (flat, raised, ridge, solid..)
    bd=4                #border depth (두꺼운 정도)
)

frame1.pack(side='top', fill='both', expand=True)

frame2=tk.Frame(window, relief='flat',bd=2) #frame object 생성
frame2.pack(side='bottom',fill='both',expand=True)#locate

button1=tk.Button(  # button object 생성
    frame1,         #window 가 아닌 frame1에 생성
    text= '프레임1'

)

button1.pack(side='right')
button2=tk.Button(frame2, text='프레임2') #button object 생성
button2.pack(side='left')


window.mainloop()

