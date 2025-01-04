from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        # Root layout
        root_widget = BoxLayout(orientation='vertical')

        # Output label for displaying input and results
        output_label = Label(size_hint_y=0.75, font_size=50, text="")

        # Button symbols
        button_symbols = (
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '.',
            '0', '*', '/', '='
        )

        # Grid layout for buttons
        button_grid = GridLayout(cols=4, size_hint_y=2)

        for symbol in button_symbols:
            button = Button(text=symbol)
            button_grid.add_widget(button)

        # Clear button
        clear_button = Button(text='Clear', size_hint_y=None, height=100)

        # Function to append button text to the output label
        def print_button_text(instance):
            if output_label.text == "Python Syntax error!":
                output_label.text = ""
            output_label.text += instance.text

        # Bind all buttons except '=' to append text
        for button in button_grid.children[::-1]:  # Reverse the order of children
            if button.text != "=":
                button.bind(on_press=print_button_text)

        # Function to resize label text dynamically
        def resize_label_text(instance, value):
            instance.font_size = 0.5 * instance.height

        output_label.bind(height=resize_label_text)

        # Function to evaluate the result
        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except Exception:
                output_label.text = "Python Syntax error!"

        # Bind the '=' button to evaluate the result
        for button in button_grid.children[::-1]:
            if button.text == "=":
                button.bind(on_press=evaluate_result)

        # Function to clear the label
        def clear_label(instance):
            output_label.text = ""

        clear_button.bind(on_press=clear_label)

        # Add widgets to the root layout
        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)

        return root_widget


# Run the app
if __name__ == "__main__":
    MyApp().run()
