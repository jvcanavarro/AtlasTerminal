from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class LoginWindow(BoxLayout):
    pass


class LoginApp(App):
    def build(self):
        return LoginWindow()


if __name__ == '__main__':
    LoginApp().run()
