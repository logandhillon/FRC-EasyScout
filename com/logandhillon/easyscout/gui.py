import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from com.logandhillon.easyscout import getResource, scan_dir


def on_image_click(_event):
    scan_dir(filedialog.askdirectory())


root = tk.Tk()
root.title("FRC EasyScout - logandhillon.com")


btn_img_main = ImageTk.PhotoImage(Image.open(getResource("1.png")).convert("RGBA"))
start_btn = tk.Label(root, image=btn_img_main, bd=0)
start_btn.bind("<Button-1>", on_image_click)

# start_btn.place(x=250, y=150)
tk.Label(root, text="click the button\nto scan :)", font=(None, 32, "bold")).pack(pady=32)
start_btn.pack(padx=64)
tk.Label(root, text="(hint: press the button)").pack(pady=32)


def start_gui(): root.mainloop()
