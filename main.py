from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button


Builder.load_file('./calculator.kv')


class CalculatorWidget(Widget):

    text = StringProperty("8")
    count = 8
  
    def clear(self):
        self.ids.input_box.text = ""       

       
    def button_value(self, number):
        prev_number = self.ids.input_box.text

        self.count -=0.019

        self.text = str(self.count)
        
        self.ids.input_box.text = f"{prev_number}{number}"

        text = self.ids.input_box.text
        if text:
            button_value = str(eval(self.ids.input_box.text))
            self.ids.input_box.text = button_value            
    
    def reset(self):
        self.ids.input_box.text = ""
             
        self.count = 8

        self.text = str(self.count)     


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
   