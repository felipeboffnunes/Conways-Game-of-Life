from kivy.app import App
from kivy.uix.widget import Widget

class FrontView(Widget):
    pass

class GameInterface(App):

    def build(self):
        return FrontView()
    