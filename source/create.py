from kivy.app import App
from kivy.uix.screenmanager import Screen


class CreateScreen(Screen):
    pass


class CreateApp(App):
    def build(self):
        return CreateScreen()


if __name__ == '__main__':
    CreateApp().run()
