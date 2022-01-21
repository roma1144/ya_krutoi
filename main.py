from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
	def build(self):

		bl = BoxLayout(orientation = 'vertical')

		bl.add_widget(TextInput())
		bl.add_widget(TextInput())
		bl.add_widget(Button())

		return bl

if __name__ == '__main__':
	MainApp().run()
