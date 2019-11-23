from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SystemWindow(BoxLayout):
    # def awesome_function(self):
    #     products_container = self.ids.products
    #     details = BoxLayout()
    #     details.add_widget()
        pass


class SystemApp(App):
    def build(self):
        return SystemWindow()


if __name__ == '__main__':
    SystemApp().run()
