import pyautogui as spam
import time

limite_msg = int(input("Enter nº de msgs: "))
msg = str(input("Coloque a msg: "))

time.sleep(5)

i = 0
while i < limite_msg:
    spam.typewrite(msg)
    spam.press("Enter")
 
    i += 1