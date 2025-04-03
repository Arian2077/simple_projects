from random import randint
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class DiceApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="Enter the number of rolls:")
        self.layout.add_widget(self.label)
        
        self.input = TextInput(multiline=False, input_filter='int')
        self.layout.add_widget(self.input)
        
        self.roll_button = Button(text="Roll Dice")
        self.roll_button.bind(on_press=self.roll_dice)
        self.layout.add_widget(self.roll_button)
        
        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)
        
        self.exit_button = Button(text="Exit")
        self.exit_button.bind(on_press=self.stop_app)
        self.layout.add_widget(self.exit_button)
        
        return self.layout

    def roll_dice(self, instance):
        try:
            rolls = int(self.input.text)
            if rolls <= 0:
                self.result_label.text = "Please enter a number greater than 0."
            else:
                results = ", ".join(str(randint(1, 6)) for _ in range(rolls))
                self.result_label.text = f"Results: {results}"
        except ValueError:
            self.result_label.text = "Invalid input. Please enter a valid number."

    def stop_app(self, instance):
        self.stop()

if __name__ == "__main__":
    DiceApp().run()