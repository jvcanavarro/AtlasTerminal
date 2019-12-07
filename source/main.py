from login import LoginScreen
from lines import LinesScreen
from system import SystemScreen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager


Builder.load_file('login.kv')
Builder.load_file('lines.kv')
Builder.load_file('system.kv')

sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(LinesScreen(name='lines'))
sm.add_widget(SystemScreen(name='system'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
