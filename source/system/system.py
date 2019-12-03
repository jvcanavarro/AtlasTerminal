from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class SystemWindow(BoxLayout):
    def add_route(self):
        container = self.ids.employees

        travel = BoxLayout(size_hint_y=None, height=30, spacing=5,
                pos_hint={'bottom':1})
        container.add_widget(travel)

        code = TextInput(multiline=False)
        code.bind(on_text_validate=self.add_route)

        name = TextInput()
        qty = TextInput()
        disc = TextInput()
        price = TextInput()
        total = TextInput()

        travel.add_widget(code)
        travel.add_widget(name)
        travel.add_widget(qty)
        travel.add_widget(disc)
        travel.add_widget(price)
        travel.add_widget(total)


class SystemApp(App):
    def build(self):
        return SystemWindow()


if __name__ == '__main__':
    SystemApp().run()
