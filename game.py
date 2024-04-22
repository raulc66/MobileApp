# game.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
class Game (BoxLayout):
    message = ObjectProperty(None)
    game_state = StringProperty('')

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

   
    def on_parent(self, _, __):
        self.start_button = self.ids['start_button']
        self.colored_blob = self.ids['colored_blob']
        self.message = self.ids['message']


    def start_game(self):
        print('Something is happening here...')
        self.message.text = 'The game has started '

    def check_color_combination(self):
        # Check if the current color combination matches the prompt
        pass

    def reveal_narrative_element(self):
        # Reveal narrative element when color combination is correct
        pass

    def reset_game(self):
        # Reset the game state
        pass
