import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from com.logandhillon import easyscout


def scan_typed(results):
    with open('out.tsv', 'a') as out:
        easyscout.write_results(results, out)


def on_start_btn(_event):
    easyscout.scan_dir(callback=scan_typed,
                       target=filedialog.askdirectory())


root = tk.Tk()
root.title("FRC EasyScout - logandhillon.com")


btn_img_main = ImageTk.PhotoImage(Image.open(easyscout.getResource("1.png")).convert("RGBA"))
start_btn = tk.Label(root, image=btn_img_main, bd=0)
start_btn.bind("<Button-1>", on_start_btn)

# start_btn.place(x=250, y=150)
tk.Label(root, text="click the button\nto scan :)", font=(None, 32, "bold")).pack(pady=32)
start_btn.pack(padx=64)
tk.Label(root, text="(hint: press the button)").pack(pady=32)


def start_gui(): root.mainloop()
