from time import sleep
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from threading import Thread, Timer
import platform
import sys
from colorama import Style
import pyautogui
from typing import List

from com.logandhillon import easyscout
from com.logandhillon.easyscout.beeper import tone

flagp = "--debug" in sys.argv
def print_debug(s: str): print(f"{Style.DIM}[easyscout] [DEBUG] {s}{Style.RESET_ALL}")


isMac = platform.system() == "Darwin"
print(f"[com.logandhillon.easyscout.gui] system has been detected as {'macOS' if isMac else 'other (likely Windows?)'}")


def countdown():
    for _ in range(4):
        tone(1500, 0.25)
        sleep(1)
    tone(1000, 0.5)


def sim_type_codes_doc(results: List[List[str]]):
    print("Starting com.logandhillon.easyscout.gui#sim_type_codes_doc")

    for tsv in results:
        max = len(tsv) - 1
        print_debug(f"NEXT ROW! {max} items ready")

        for i, cell in enumerate(tsv):
            print_debug(f"printing cell {i}: {cell.encode()}")
            pyautogui.write(cell)
            sleep(0.1)
            pyautogui.press("enter" if i == max else "tab") 

        print_debug("row complete, going next")
        sleep(0.1)
        pyautogui.press("left", max+1)


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
    if "--debug-hid" in sys.argv:
        for i in range(3):
            print(f"HID FUNC-TEST WILL START IN {3-i} SECONDS.")
            sleep(1)

        sim_type_codes_doc([["cell", "cell 2"], ["cell", "cell 2"], ["cell", "cell 2"]])
        print("test complete :)")
        exit()
