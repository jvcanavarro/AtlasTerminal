from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class CreateAccountScreen(Screen):
    def create_user(self):
        login = self.manager.get_screen('login')
        accounts = login.accounts
        emails = login.emails

        info = self.ids.info
        username = self.ids.username
        email = self.ids.email
        password = self.ids.password
        conf_password = self.ids.conf_password


        if username.text and email.text and password.text and conf_password.text:
            if password.text != conf_password.text:
                info.text = 'Senhas diferentes'

            elif (username.text, password.text) not in accounts.items() and email not in emails:
                accounts[username.text] = password.text
                emails[username.text] = email.text
                info.text = 'Conta criada'

            else:
                info.text = 'Conta já existente'

        else:
            info.text = 'Campos faltando'


class ForgotPasswordScreen(Screen):
    def send_recovery_email(self):
        email = self.ids.recovery_email
        info = self.ids.info
        login = self.manager.get_screen('login')
        emails = login.emails
        if email.text in emails.values():
            info.text = 'Email enviado'
        else:
            info.text = 'Email não registrado'


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accounts = {'admin': 'admin'}
        self.emails = {'admin': 'admin@admin.com'}

    def validate_user(self):
        username = self.ids.username_field
        password = self.ids.password_field
        info = self.ids.info

        if (username.text, password.text) in self.accounts.items():
            self.manager.current = 'lines'
            username.text = ''
            password.text = ''
        else:
            print(self.accounts)
            info.text = '[color=#FF0000]Usuário não Registrado ou Senha Incorreta[/color]'


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
