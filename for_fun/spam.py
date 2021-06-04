import pyautogui
from time import sleep

def typecum(num):
    pyautogui.click(3236,343)
    pyautogui.typewrite("cum " + str(num))
    pyautogui.click(3244,440)
    pyautogui.click(2736,19)
    pyautogui.typewrite("https://docs.google.com/forms/d/e/1FAIpQLSfgD54hHTGUEaeUbhNeZTC1T_qATf3v0jguGCQnpOjOlFRDDw/viewform?fbzx=4301294213172193961")
    pyautogui.click(2690,20)
    pyautogui.press('enter')
    sleep(1)
    
def spam_cum():
    pyautogui.click(905, 955)
    pyautogui.typewrite("cum")
    pyautogui.press('enter')
for i in range(100):
    spam_cum()
    
