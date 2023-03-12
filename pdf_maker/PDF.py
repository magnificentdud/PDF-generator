import tkinter as tk
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Award')

window.geometry("300x400+100+100")
window.resizable(True, True)

#입력
def entry_event_fn(user_input):
    label.config(text='{}'.format(entry.get()))


#frame making

#frame 1
frame1=tk.Frame(window, relief='flat',bd=2) #frame object 생성
frame1.pack(side='bottom',fill='both',expand=True)#locate

#frame 2
frame2=tk.Frame(window, relief='flat',bd=2) #frame object 생성
frame2.pack(side='bottom',fill='both',expand=True)#locate


src = cv2.imread("image.jpeg") #image read
src = cv2.resize(src, (320,240))
src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

#convert numpy image into tk image
img = Image.fromarray(src)
imgtk = ImageTk.PhotoImage(image=img)

label = tk.Label(window, image=imgtk) # label 에 tk를 등록
label.pack() #locate



entry = tk.Entry(window)
entry.bind('<Return>',entry_event_fn)
entry.pack()

add_text_button = tk.Button(frame1, text='Add text')
add_text_button.pack(side = 'left', expand = True, fill = 'both')

add_image_button = tk.Button(frame1, text = 'Add image')
add_image_button.pack(side = 'right', expand = True, fill = 'both')

load_button = tk.Button(frame2, text='Load')
load_button.pack(side = 'left', expand = True, fill = 'both')

close_button = tk.Button(frame2, text = 'Close')
close_button.pack(side = 'right', expand = True, fill = 'both')




window.mainloop()