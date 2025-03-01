import platform
import sys
import tkinter as tk
from threading import Thread, Timer
from time import sleep
from tkinter import filedialog, messagebox
from typing import List

import pyautogui
from colorama import Style
from PIL import Image, ImageTk

from com.logandhillon import easyscout
from com.logandhillon.easyscout.beeper import tone
from com.logandhillon.easyscout.debug import hid

FLAG_DEBUG = "--debug" in sys.argv
Thread(target=hid.print_keys_down).start()


def print_debug(s: str):
    if FLAG_DEBUG:
        print(f"{Style.DIM}[{__file__[__file__.find('com'):]}] [DEBUG] {s}{Style.RESET_ALL}")


isMac = platform.system() == "Darwin"
print(f"[com.logandhillon.easyscout.gui] system has been detected as {'macOS' if isMac else 'other (likely Windows?)'}")

if isMac:
    print("macOS is NOTTT supported 😭 gg")
    exit()


def countdown():
    for _ in range(4):
        tone(1500, 0.25)
        sleep(1)
    tone(1000, 0.5)


def sim_type_codes_doc(results: List[str]):
    print("Starting com.logandhillon.easyscout.gui#sim_type_codes_doc")

    for i, datastring in enumerate(results):
        print_debug(f"NEXT ROW! {len(datastring)} bytes ready")

        print_debug(f"printing cell {i}: {datastring.encode()}")
        pyautogui.write(datastring)
        pyautogui.press("return")

        print_debug("row complete, going next")
        pyautogui.press("left", len(datastring.split("\t")))


def handle_btn(results):
    # please ignore this devious one-liner 😭
    messagebox.showinfo("Heads up!", "EasyScout will now enter these values into your scouting datasheet.\n\nPlease click the first column of the first empty row and press OK.\n\nAfter pressing OK, EasyScout will begin in 5 seconds.")
    print("Preparing to simulate HID input...")
    Thread(target=countdown).start()
    Timer(5, function=sim_type_codes_doc, args=(results,)).start()


def on_start_btn(_event):
    easyscout.scan_dir(callback=handle_btn, target=filedialog.askdirectory())


root = tk.Tk()
root.title("FRC EasyScout - logandhillon.com")


btn_img_main = ImageTk.PhotoImage(Image.open(easyscout.getResource("1.png")).convert("RGBA"))
start_btn = tk.Label(root, image=btn_img_main, bd=0)
start_btn.bind("<Button-1>", on_start_btn)

tk.Label(root, text="click the button\nto scan :)", font=(None, 32, "bold")).pack(pady=32)
start_btn.pack(padx=64)
tk.Label(root, text="(hint: press the button)").pack(pady=32)


def start_gui():
    root.mainloop()


if __name__ == "__main__":
    if "--test-hid" in sys.argv:
        for i in range(3):
            print(f"HID FUNC-TEST WILL START IN {3-i} SECONDS.")
            sleep(1)

        sim_type_codes_doc([["cell", "cell 2"], ["cell", "cell 2"], ["cell", "cell 2"]])
        print("test complete :)")
        exit()
