from kivy.app import App
from kivy.uix.screenmanager import Screen


class LinesScreen(Screen):
    pass


class LinesApp(App):
    def build(self):
        return LinesScreen()


if __name__ == '__main__':
    LinesApp().run()
