from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.properties import ( NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock


class Angle(Slider):

    min = NumericProperty(0.)
    max = NumericProperty(0.)
    value = NumericProperty(0.)
    size_hint_x = NumericProperty(0.)


    open = ObjectProperty()




class Bt1(Button):

    bt1 = ObjectProperty()





class manager(Widget):
    flash = ObjectProperty(None)
    one = ObjectProperty(None)


class mApp(App):
    def build(self):
        menu1 = manager()
        return menu1


if __name__ == '__main__':
    mApp().run()





