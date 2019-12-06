from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class LoginWindow(BoxLayout):
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.password_field
        info = self.ids.info

        username = user.text
        password = pwd.text

        if username == '' or password == '':
            info.text = '[color=#FF0000]username and password required[/color]'


class LoginApp(App):
    def build(self):
        return LoginWindow()


if __name__ == '__main__':
    LoginApp().run()
