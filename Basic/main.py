from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import json, glob
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')



class LoginScreen(Screen):
    def sign_up(self):
       self.manager.current = "sign_up_screen"
    def login(self, uname,pword):
        self.manager.current = 'login_screen_success'

    


class RootWidget(ScreenManager):

    pass
class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.current = "login_screen"
    def get_quote(self, feel):
        feel = feel.lower()
        if feel =='happy':
            with open("C:\\Users\\ssubh\\OneDrive\\Desktop\\python\\Basic\\mobile app\\happy.txt",'r', encoding="utf8") as file:
                feels = file.readlines()
                self.ids.quote.text =  random.choice(feels)
        elif feel =='sad':
            with open("C:\\Users\\ssubh\\OneDrive\\Desktop\\python\\Basic\\mobile app\\sad.txt",'r', encoding="utf8") as file:
                feels = file.readlines()
                self.ids.quote.text =  random.choice(feels)
        elif feel =='unloved':
            with open("C:\\Users\\ssubh\\OneDrive\\Desktop\\python\\Basic\\mobile app\\unloved.txt",'r', encoding="utf8") as file:
                feels = file.readlines()
                self.ids.quote.text =  random.choice(feels)
    




class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen"
class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("C:\\Users\\ssubh\\OneDrive\\Desktop\\python\\Basic\\mobile app\\login.json") as file:
            users = json.load(file)
        users[uname] = {'username':uname, 'password':pword,'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        self.manager.current = "sign_up_scree_success"



class ImageButton(HoverBehavior, Image, ButtonBehavior):
    pass

class main_app(App):
    def build(self):
        return RootWidget()


if __name__=="__main__":
    main_app().run()