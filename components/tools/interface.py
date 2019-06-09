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
# COMPONENTS
from components.config.raw_python_seed_generator import create_seed
from components.logic.universe import Universe
from .visualizer import plot_states


class GameInterface(App):

    def build(self):

        Window.size = (140, 100)

        # Axis
        label_x = Label(text='x')
        label_y = Label(text='y')
        environment_axis_x = TextInput(text='10')
        environment_axis_y = TextInput(text='10')

        # Layout
        layout = BoxLayout(orientation='vertical', spacing=10)
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
            for row, y in enumerate(range(int(environment_axis_x.text))):
                row = BoxLayout()
                for i in range(int(environment_axis_y.text)):
                    c = CheckBox(id=str(i))
                    row.add_widget(c)
                rows.add_widget(row)
            layout.add_widget(rows)
            # Remove last config
            layout.remove_widget(layout_axis_x)

            layout.remove_widget(layout_axis_y)
            layout.remove_widget(create_grid_button)
            # Add new config
            layout_simulation = BoxLayout(size_hint=(1, .1))
            label_simulation = Label(text='Simulation time')
            simulation_time = TextInput(text='10')
            layout_simulation.add_widget(label_simulation)
            layout_simulation.add_widget(simulation_time)
            layout.add_widget(layout_simulation)

            def run_simulation(instance):
                # CREATE SEED
                # layout.children[2] is the simulation
                # layout.children[2].children are the y rows
                # each y row has x checkboxes
                simulation_id = []
                simulation_status = []
                for i, _ in enumerate(layout.children[2].children):
                    cell_id = [
                        checkbox.id for checkbox in layout.children[2].children[i].children]
                    cell_status = [
                        checkbox.active for checkbox in layout.children[2].children[i].children]
                    simulation_id.append(cell_id)
                    simulation_status.append(cell_status)
            
                seed = create_seed(simulation_id, simulation_status)

                # RUN
                u = Universe(int(environment_axis_x.text),
                             int(environment_axis_y.text),
                             seed=seed)
                for _ in range(int(simulation_time.text)):
                    u.iterate()
                plot_states()

            run_simulation_button = Button(
                text='Run Game of Life', size_hint=(1, .12))
            run_simulation_button.bind(on_press=run_simulation)
            layout.add_widget(run_simulation_button)
            Window.size = (int(environment_axis_x.text)*12 + 200,
                           int(environment_axis_y.text)*30 + 200)

        create_grid_button = Button(text='Create Environment')
        create_grid_button.bind(on_press=create_grid)

        layout.add_widget(create_grid_button)
        return layout
