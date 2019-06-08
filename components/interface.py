from kivy.app import App
# UIX
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
# CORE
from kivy.core.window import Window


class GameInterface(App):

    def build(self):
        Window.size = (140, 100)

        # Axis
        label_x = Label(text='x')
        label_y = Label(text='y')
        environment_axis_x = TextInput(text='10')
        environment_axis_y = TextInput(text='10')

        # Layout
        layout = BoxLayout(orientation='vertical')
        layout_axis_x = BoxLayout()
        layout_axis_x.add_widget(label_x)
        layout_axis_x.add_widget(environment_axis_x)
        layout_axis_y = BoxLayout()
        layout_axis_y.add_widget(label_y)
        layout_axis_y.add_widget(environment_axis_y)
        layout.add_widget(layout_axis_x)
        layout.add_widget(layout_axis_y)

        def create_grid(instance):
            # Grid
            rows = BoxLayout(orientation='vertical')
            for row in range(int(environment_axis_x.text)):
                row = BoxLayout()
                for _ in range(int(environment_axis_y.text)):
                    c = CheckBox()
                    row.add_widget(c)
                rows.add_widget(row)

            layout.add_widget(rows)
            Window.size = (int(environment_axis_x.text)*12 + 200,
                           int(environment_axis_y.text)*30 + 200)
                           
        create_grid_button = Button(text='Create Environment')
        create_grid_button.bind(on_press=create_grid)

        layout.add_widget(create_grid_button)
        return layout
