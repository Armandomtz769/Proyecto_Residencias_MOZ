from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.listview import ListView, ListAdapter
from kivy.uix.listview import ListItemButton


class PedimentosTable(Screen):
    """ Pantalla de la tabla de Pedimentos """

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        self.data = data if data else []

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Barra superior con botón de regreso
        header_layout = BoxLayout(orientation="horizontal", size_hint_y=0.1)

        self.back_button = Button(text="←", size_hint_x=0.2)
        self.back_button.bind(on_press=self.go_back)

        self.title_label = Label(text="Resultados de Búsqueda", size_hint_x=0.8, font_size=18, bold=True)

        header_layout.add_widget(self.back_button)
        header_layout.add_widget(self.title_label)

        layout.add_widget(header_layout)

        # Lista de Pedimentos
        self.list_view = ListView(size_hint_y=0.9)
        self.list_adapter = ListAdapter(
            data=[f"{item[0]} - {item[1]} - {item[2]}" for item in self.data],
            cls=ListItemButton,
            args_converter=self.args_converter
        )
        self.list_view.adapter = self.list_adapter

        layout.add_widget(self.list_view)
        self.add_widget(layout)

    def args_converter(self, row_index, item):
        """ Convierte los datos para mostrarlos en la lista """
        return {'text': item, 'size_hint_y': None, 'height': 40}

    def go_back(self, instance):
        """ Regresa a la pantalla de búsqueda """
        self.manager.current = "search"
