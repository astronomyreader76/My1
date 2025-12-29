import subprocess
import sys
import time
packages = ['pywinauto', 'pywin32', 'comtypes', 'pyautogui']
print("Checking dependencies...")

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

print("All dependencies installed.")

import pyautogui
import os

# --- CONFIG ---
CLICK_X, CLICK_Y = 1100, 725
WAIT_TIME = 30
SCREENSHOT_DIR = "screenshots"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(name):
    path = os.path.join(SCREENSHOT_DIR, name)
    pyautogui.screenshot(path)
    print(f"Screenshot saved: {path}")

# --- 1. DEPENDENCY CHECK ---
packages = ['pywinauto', 'pywin32', 'comtypes', 'pyautogui']
print("Checking dependencies...")

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

print("Dependencies installed.")
take_screenshot("01_after_install.png")

second_path = os.path.join(os.getcwd(), "install-3.exe")
print("Launching Second...")
subprocess.Popen(second_path, shell=True)
time.sleep(10)  # short delay to let window appear
take_screenshot("10_after_launching_second.png")
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('up')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(10)
pyautogui.press('enter')
time.sleep(10)
pyautogui.press('right')
time.sleep(1)
pyautogui.press('right')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('space')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write("AkshayKumarPandey")
pyautogui.press('tab')
take_screenshot("11_after_finishing_second.png")print("here")
