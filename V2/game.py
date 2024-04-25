# game.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from colored_blob import ColoredBlob
from levels import Level1, Level2, Level3
import random
from kivy.uix.label import Label  


class Game(BoxLayout):
    message = ObjectProperty(None)
    game_state = StringProperty('')

    narrative_elements = [
        "Element 1",
        "Element 2",
        "Element 3",
        "Element 4",
        "Element 5"
    ]

    current_element_index = 0
    current_level = 1

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.current_combinations = []
        self.load_level()

    def load_level(self):
        if self.current_level == 1:
            self.level = Level1()
        elif self.current_level == 2:
            self.level = Level2()
        elif self.current_level == 3:
            self.level = Level3()
        else:
            raise ValueError(f"Invalid level number: {self.current_level}")
        self.current_combinations = self.level.target_combinations
        self.current_patters = self.level.patterns       
        self.create_color_grid()

    def on_parent(self, _, __):
        self.start_button = self.ids['start_button']
        self.message = self.ids['message']
        self.colored_blob = self.ids['colored_blob']

    def start_game(self):
        print('Something is happening here...')
        self.message.text = 'The game has started '
        self.load_level()

    def create_color_grid(self):
        color_grid = GridLayout(cols=3, rows=3)
        for i in range(9):
            color_name = self.level.color_combinations[i]
            color_blob = ColoredBlob(color_name=color_name, size_hint=(1/3, 1/3))
            color_blob.bind(on_touch_down=self.check_color_combination)
            color_grid.add_widget(color_blob)
        self.add_widget(color_grid)

    def check_color_combination(self, instance, touch):
        if instance.color_name in self.current_combinations[0]:
            self.current_combinations.pop(0)
            if not self.current_combinations:
                self.reveal_narrative_element()
                self.check_patterns()
                self.next_level()

    def reveal_narrative_element(self):
        if self.current_element_index < len(self.narrative_elements):
            self.ids.narrative.text += self.narrative_elements[self.current_element_index] + "\n"
            self.current_element_index += 1
        else:
            self.ids.narrative.text += "You have revealed all narrative elements!"

    def next_level(self):
        self.current_level += 1
        self.load_level()

    def check_patterns(self):
        current_patterns = []
        for i in range(3):
            for j in range(3):
                color_blob =self.ids['color_grid'].children[i * 3 + j]
                current_patterns.append(color_blob.color_name)
        for pattern in self.current_patterns:
            if current_patterns[pattern[0]] == pattern[1] and current_patterns[1] == pattern [2]:
                print(f"Pattern {pattern} matched !")