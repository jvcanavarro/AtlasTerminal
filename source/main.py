from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class CreateAccountScreen(Screen):
    pass


class ForgotPasswordScreen(Screen):
    pass


class LoginScreen(Screen):
    def validate_user(self):
        username = self.ids.username_field
        password = self.ids.password_field
        info = self.ids.info

        if username.text == '' or password == '':
            info.text = '[color=#FF0000]Username and Password required[/color]'
        else:
            self.manager.current = 'lines'


class LinesScreen(Screen):
    pass


class SystemScreen(Screen):
    def add_route(self):
        route = BoxLayout(size_hint_y=None, height=30, spacing=5)

        for i in range(10):
            route.add_widget(TextInput())

        container = self.ids.travels
        container.add_widget(route)


class ManagerApp(App):
    def build(self):
        Builder.load_file('design/system.kv')
        Builder.load_file('design/lines.kv')
        Builder.load_file('design/create.kv')
        Builder.load_file('design/forgot.kv')
        Builder.load_file('design/login.kv')

        manager = ScreenManager()

        manager.add_widget(LoginScreen(name='login'))
        manager.add_widget(CreateAccountScreen(name='create'))
        manager.add_widget(ForgotPasswordScreen(name='forgot'))
        manager.add_widget(LinesScreen(name='lines'))
        manager.add_widget(SystemScreen(name='system'))
        return manager


if __name__ == '__main__':
    ManagerApp().run()
