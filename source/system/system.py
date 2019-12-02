from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class SystemWindow(BoxLayout):
    def awesome_function(self):
        code = self.ids.code_input.text
        products_container = self.ids.products
        if code == '1234':
            details = BoxLayout(size_hint_y=None, height=30, pos_hint={'top': 1})
            products_container.add_widget(details)

            code = Label(text=code, size_hint_x=.2, color=(.06, .45, .45, 1))
            name = Label(text='Product One', size_hint_x=.3, color=(.06, .45, .45, 1))
            qty = Label(text='1', size_hint_x=.1, color=(.06, .45, .45, 1))
            disc = Label(text='0.00', size_hint_x=.1, color=(.06, .45, .45, 1))
            price = Label(text='0.00', size_hint_x=.1, color=(.06, .45, .45, 1))
            total = Label(text='0.00', size_hint_x=.2, color=(.06, .45, .45, 1))


            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)

            # Update Preview
            product_name = 'Product One: '
            product_price = 1.00
            preview = self.ids.receipt_preview
            preview_text = preview.text
            under_prev = preview_text.find('`')

            if under_prev > 0:
                preview_text = preview_text[:under_prev]

            purchase_total = '`\n\nTotal: 0.0'
            new_preview = '\n'.join([preview_text, product_name +
                str(product_price), purchase_total])
            preview.text = new_preview


class SystemApp(App):
    def build(self):
        return SystemWindow()


if __name__ == '__main__':
    SystemApp().run()
