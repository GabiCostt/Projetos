import pyautogui
from time import sleep

pyautogui.press('win')
sleep(1)
pyautogui.typewrite('Prompt de comando')
pyautogui.press('enter')
sleep(2)
pyautogui.typewrite('shutdown -s')
pyautogui.press('enter')