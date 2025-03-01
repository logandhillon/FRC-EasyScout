import sys
from colorama import Style
import keyboard


is_debug = "--debug-keydown" in sys.argv


def print_key(e):
    if is_debug:
        print(f"{Style.DIM}[debug.hid] [DEBUG] KEY PRESS! : {e.name} ({e}){Style.RESET_ALL}")


def print_keys_down():
    keyboard.on_press(print_key)
    keyboard.wait()
