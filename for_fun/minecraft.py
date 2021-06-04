import pyautogui
import pydirectinput
from time import sleep

def break_block(blocks):
    for i in range(blocks):
        pydirectinput.mouseDown()
        sleep(.8)
        pydirectinput.mouseUp()
        pydirectinput.keyDown('w')
        sleep(0.5)
        pydirectinput.keyUp('w')
        pydirectinput.mouseDown()
        sleep(.8)
        pydirectinput.mouseUp()
def dirt_blk(blocks, rows):
    for i in range(rows):
        for i in range(blocks):
            pydirectinput.mouseDown()
            sleep(1.1)
            pydirectinput.mouseUp()
            pydirectinput.keyDown('w')
            sleep(0.1425)
            pydirectinput.keyUp('w')
        secs = (blocks)/ 4.194630872483222 + 0.5
        pydirectinput.keyDown('s')
        sleep(secs)
        pydirectinput.keyUp('s')
        pydirectinput.keyDown('a')
        sleep(0.15)
        pydirectinput.keyUp('a')

pyautogui.click(812,702)
pyautogui.click(628,224)

break_block(60)

