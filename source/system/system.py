from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SystemWindow(BoxLayout):
    pass


class SystemApp(App):
    def build(self):
        return SystemWindow()


if __name__ == '__main__':
    SystemApp().run()
