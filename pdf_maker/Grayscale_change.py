import tkinter as tk
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.title("My First GUI")
window.geometry("320x400+100+100")

# src = cv2.imread("image.jpeg") #image read
# src = cv2.resize(src, (320,240))
# src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

#convert numpy image into tk image
width = 320
height = 320
color_image = cv2.imread('image.jpeg')
color_image = cv2.resize(color_image, (width, height))
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

def np_image_to_tk_image(np_image):
    img = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    return imgtk

imgtk = np_image_to_tk_image(color_image)
label = tk.Label(window, image=imgtk) #register tk image
label.pack()


#define the color
def color_tk_image():
    imgtk  = np_image_to_tk_image(color_image)
    label.config(image=imgtk)
    label.image=imgtk

#change color to grayscale

# button1 = tk.Button(
#     window,
#     text='hello'

# )
# button1.pack(side='left')

def gray_scale_tk_image():
    imgtk  = np_image_to_tk_image(gray_image)
    label.config(image=imgtk)
    label.image=imgtk

button1 = tk.Button(
    window, 
    text = 'Grayscale',
    width = 15,
    height = 2,
    command = gray_scale_tk_image
)
button1.pack()

button2 = tk.Button(
    window, 
    text = 'Color',
    width = 15,
    height = 2,
    command = color_tk_image
)
button2.pack()




window.mainloop()
