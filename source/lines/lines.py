from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class LinesWindow(BoxLayout):
    pass


class LinesApp(App):
    def build(self):
        return LinesWindow()


if __name__ == '__main__':
    LinesApp().run()
