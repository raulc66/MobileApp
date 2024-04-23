# game.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from colored_blob import ColoredBlob

class Game(BoxLayout):
    message = ObjectProperty(None)
    game_state = StringProperty('')

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

    def on_parent(self, _, __):
        self.start_button = self.ids['start_button']
        self.message = self.ids['message']

    def start_game(self):
        self.message.text = 'The game has started '
        self.create_color_grid()

    def create_color_grid(self):
        color_grid = GridLayout(cols=3, rows=3)
        for i in range(9):
            color_name = 'red' if i % 2 == 0 else 'blue'  # For example, assigning colors randomly
            color_grid.add_widget(ColoredBlob(color_name=color_name))
        self.add_widget(color_grid)