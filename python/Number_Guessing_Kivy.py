from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from random import randint


class NumberGuessingGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Generate random target number
        self.target_number = randint(1, 100)

        # Input label and field
        self.label = Label(text="Enter your number:", font_size=20)
        self.add_widget(self.label)

        self.input_field = TextInput(font_size=20, multiline=False)
        self.add_widget(self.input_field)

        # Guess button
        self.guess_button = Button(text="Guess", font_size=20, size_hint=(1, 0.2))
        self.guess_button.bind(on_press=self.guess_number)
        self.add_widget(self.guess_button)

        # Result display
        self.result_label = Label(text="", font_size=18)
        self.add_widget(self.result_label)

    def guess_number(self, instance):
        try:
            num = int(self.input_field.text)
        except ValueError:
            self.result_label.text = "Please enter a valid integer."
            return

        if num < 1 or num > 100:
            self.result_label.text = "Please enter a number between 1 and 100."
        elif num < self.target_number:
            self.result_label.text = f"{num} is too low."
        elif num > self.target_number:
            self.result_label.text = f"{num} is too high."
        else:
            self.result_label.text = f"Congratulations! {num} is correct."
            self.target_number = randint(1, 100)  # Reset target number


class NumberGuessingApp(App):
    def build(self):
        return NumberGuessingGame()


if __name__ == "__main__":
    NumberGuessingApp().run()
