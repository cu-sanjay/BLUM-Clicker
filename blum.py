import pyautogui
import pygetwindow as gw
import time
import keyboard
import random
import sys
from pynput.mouse import Button, Controller

delay = int(sys.argv[1]) if len(sys.argv) > 1 else 2
window_name_input = sys.argv[2] if len(sys.argv) > 2 else "1"

if window_name_input == '1':
    window_name = "TelegramDesktop"
else:
    window_name = window_name_input

mouse = Controller()

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

print('Starting the $BLUM Auto Clicker...')
time.sleep(delay)
print('🚀 | $BLUM Clicker started.\nℹ️ | Press Q to Pause, Z to Stop.')

paused = False

while True:
    if keyboard.is_pressed('q'):
        paused = not paused
        if paused:
            print('⏸️ | Paused. Press Q to Restart.')
        else:
            print('🤖 | Resuming...')
        time.sleep(0.2)

    if keyboard.is_pressed('z'):
        print("❤️ | Exiting... Thanks for using Blum Automation! Follow: github.com/cu-sanjay")
        break

    if paused:
        continue

    check = gw.getWindowsWithTitle(window_name)
    if not check:
        print(f"[❌] | Window - {window_name} not found! Waiting for it to restart...")
        while not check:
            time.sleep(1)
            check = gw.getWindowsWithTitle(window_name)
        print(f"[✅] | Window found - {window_name}\n[✅] | Press 'q' to pause.")

    telegram_window = check[0]

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    if telegram_window:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True

print('🔚 | Stopped.')
