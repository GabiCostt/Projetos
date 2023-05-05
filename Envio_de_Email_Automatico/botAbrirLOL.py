import pyautogui as pg
import time

pg.PAUSE = 2
time.sleep(3)

pg.press('win')
pg.typewrite("lol")
pg.press('enter')
time.sleep(30)
pg.click(x=175, y=45)