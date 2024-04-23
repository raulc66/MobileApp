# colored_blob.py

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from colors import color_list
from kivy.properties import StringProperty

class ColoredBlob(Widget):
    color_name = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.color_name = kwargs.get('color_name')
        self.color_rgb = next(filter(lambda c: c['name'] == self.color_name, color_list))['rgb']
        self.color_label = Label(text=self.color_name, color=self.color_rgb, font_size=16)
        self.add_widget(self.color_label)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(f"Colored Blob {self.color_name} was clicked!")
            return True
        return super().on_touch_down(touch)