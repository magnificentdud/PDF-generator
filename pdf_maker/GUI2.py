import tkinter as tk

window = tk.Tk()

window.title('MyfirstGUI')
window.geometry('{}x{}+{}+{}'.format(300,300,100,100))

#[1] pack: 상대 위치 배치
'''
b1 = tk.Button(window, text = 'top')
b1_1 = tk.Button(window, text = 'top-1')
b2 = tk.Button(window, text = 'bottom')
b2_2 = tk.Button(window, text = 'bottom-1')

b1.pack(side = 'top')
b1_1.pack(side= 'top', fill = 'x')

b2.pack(side = 'bottom')
b2_2.pack(side= 'bottom', anchor = 'e')
'''

#[2] grid: 셀 단위 배치
'''
b1 = tk.Button(window, text = '(0,0)')
b2 = tk.Button(window, text = '(0,1)')
b3 = tk.Button(window, text = '(0,2)', width=10)
b4 = tk.Button(window, text = '(1,0)')
b5 = tk.Button(window, text = '(1,1)')
b6 = tk.Button(window, text = '(1,2)')

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0, rowspan=2)
b5.grid(row=1,column=1, columnspan=3)
b6.grid(row=1,column=2)
'''

#[3] place: 절대 위치 배치

b1 = tk.Button(window, text = '(50,50)')
b2 = tk.Button(window, text = '(50,100)')
b3 = tk.Button(window, text = '(0,200)')
b4 = tk.Button(window, text = '(1,300)')

b1.place(x=50,y=50)
b2.place(x=50,y=100, width=100)
b3.place(x=0,y=200, relwidth=0.5)
b4.place(x=0,y=300,relx=0.5)

window.mainloop()