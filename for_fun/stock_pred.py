import pyautogui as pgui
from time import sleep
import pandas as pd

song = pd.read_csv(r'C:\\Users\\ssubh\\OneDrive\\Desktop\\python\\for_fun\\lucid_dreams.csv')
pgui.click(757,698)

words = len(song)

for i in range(words):
    pgui.click(603,613)
    pgui.typewrite(song.loc[i,"Words"])   
    pgui.press('enter') 

# for i in range(2):
#     pgui.click(579,613)
#     pgui.hotkey('ctrl', 'v')
#     pgui.press('enter')
