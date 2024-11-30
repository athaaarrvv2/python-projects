import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageFilter

root = tk.Tk()

root.geometry("1280x698")
root.minsize(1280, 698)
root.maxsize(1920, 1080)

root.iconbitmap("img/logo.ico")
root.title("Makhanlal Chaturvedi National University of Journalism and Communication, Bhopal")

img_blur = Image.open("img/bg_img.jpg")
img_filter = img_blur.filter(ImageFilter.GaussianBlur(5))

img_blured = ImageTk.PhotoImage(img_filter)

img_label = Label(root, image=img_blured)
img_label.place(x=0, y=0, relwidth=1, relheight=1)

img_label.pack()

root.mainloop()