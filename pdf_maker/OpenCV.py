import tkinter as tk
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.title("My First GUI")
window.geometry("320x240+100+100")

src = cv2.imread("image.jpeg") #image read
src = cv2.resize(src, (320,240))
src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

#convert numpy image into tk image
img = Image.fromarray(src)
imgtk = ImageTk.PhotoImage(image=img)

label = tk.Label(window, image=imgtk) # label 에 tk를 등록
label.pack() #locate

window.mainloop()
