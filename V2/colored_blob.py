# colored_blob.py

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from colors import color_list
from kivy.properties import StringProperty
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock   
class ColoredBlob(Widget):
    color_name = StringProperty('')
    effect = StringProperty('')

    def __init__(self, color_name, **kwargs):
        super().__init__(**kwargs)
        self.color_name = color_name
        with self.canvas:
            Color(1, 1, 1, 1)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)

    def set_color(self, color):
        with self.canvas:
            self.ellipse.color = color

    def on_size(self, *args):
        self.ellipse.size = self.size

    def on_pos(self, *args):
        self.ellipse.pos = self.pos

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.effect = 'clicked'
            Clock.schedule_once(self.reset_effect, 0.2)
            return True
        return super().on_touch_down(touch)

    def reset_effect(self, dt):
        self.effect = ''