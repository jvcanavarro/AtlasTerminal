from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class SystemWindow(BoxLayout):
    def add_route(self):
        travel = BoxLayout(size_hint_y=None, height=30, spacing=5)

        travel.add_widget(TextInput())
        travel.add_widget(TextInput())
        travel.add_widget(TextInput())
        travel.add_widget(TextInput())
        travel.add_widget(TextInput())
        travel.add_widget(TextInput())
        travel.add_widget(TextInput())
        travel.add_widget(TextInput())
        travel.add_widget(TextInput())
        travel.add_widget(TextInput())

        container = self.ids.travels
        container.add_widget(travel)



class SystemApp(App):
    def build(self):
        return SystemWindow()


if __name__ == '__main__':
    SystemApp().run()
