from time import sleep
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from threading import Thread

from com.logandhillon import easyscout
from com.logandhillon.easyscout.beeper import tone


def countdown():
    for i in range(7):
        tone(1500, 0.25)
        sleep(1)
    tone(1000, 0.5)


def sim_type_codes_doc(results):
    # please ignore this devious one-liner 😭
    messagebox.showinfo("Heads up!", "EasyScout will now enter these values into your scouting datasheet.\n\nPlease click the first column of the first empty row and press OK.\n\nAfter pressing OK, EasyScout will begin in 8 seconds.")
    Thread(target=countdown).start()


def on_start_btn(_event):
    easyscout.scan_dir(callback=sim_type_codes_doc,
                       target=filedialog.askdirectory())


root = tk.Tk()
root.title("FRC EasyScout - logandhillon.com")


btn_img_main = ImageTk.PhotoImage(Image.open(easyscout.getResource("1.png")).convert("RGBA"))
start_btn = tk.Label(root, image=btn_img_main, bd=0)
start_btn.bind("<Button-1>", on_start_btn)

tk.Label(root, text="click the button\nto scan :)", font=(None, 32, "bold")).pack(pady=32)
start_btn.pack(padx=64)
tk.Label(root, text="(hint: press the button)").pack(pady=32)


def start_gui(): root.mainloop()
