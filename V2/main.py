# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Import classes and functions from other files
from game import Game

# Load UI layout from kv file
Builder.load_file('ui.kv')

class ColorHarmonyApp(App):
    def build(self):
        # Create game instance
        game = Game()
        
        # Create and return root widget
        return game
if __name__ == '__main__':
    ColorHarmonyApp().run()
