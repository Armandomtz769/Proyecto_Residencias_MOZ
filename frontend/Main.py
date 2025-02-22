from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.calendar import CalendarWidget
from kivy.uix.radio import RadioButton
from kivy.uix.popup import Popup
from ShipmentsList import PedimentosTable

class SearchScreen(Screen):
    """ Pantalla de búsqueda de pedimentos """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Búsqueda por Fecha
        self.date_radio = RadioButton(group='search_type', text='Búsqueda por fecha')
        self.date_radio.bind(on_press=self.toggle_calendar)
        layout.add_widget(self.date_radio)

        self.start_date = TextInput(hint_text="Inicio: dd/mm/aaaa", multiline=False)
        layout.add_widget(self.start_date)

        self.end_date = TextInput(hint_text="Fin: dd/mm/aaaa", multiline=False)
        layout.add_widget(self.end_date)

        self.calendar = CalendarWidget()
        self.calendar.bind(on_select=self.set_date)
        layout.add_widget(self.calendar)

        # Búsqueda por Referencia
        self.ref_radio = RadioButton(group='search_type', text='Búsqueda por referencia')
        layout.add_widget(self.ref_radio)

        self.reference_input = TextInput(hint_text="Referencia: ALMI24-00000", multiline=False)
        layout.add_widget(self.reference_input)

        # Botón de búsqueda
        self.search_button = Button(text="Buscar", size_hint=(1, 0.2))
        self.search_button.bind(on_press=self.search_reference)
        layout.add_widget(self.search_button)

        self.add_widget(layout)

    def toggle_calendar(self, instance):
        """ Muestra u oculta el calendario según la opción elegida """
        self.calendar.opacity = 1 if self.date_radio.active else 0
        self.calendar.disabled = not self.date_radio.active

    def set_date(self, instance, date):
        """ Asigna la fecha seleccionada en los campos de texto """
        if not self.start_date.text:
            self.start_date.text = date.strftime("%d/%m/%Y")
        else:
            self.end_date.text = date.strftime("%d/%m/%Y")

    def search_reference(self, instance):
        """ Busca la referencia o rango de fechas ingresado y muestra los resultados """
        reference = "ALMI" + self.reference_input.text.strip().upper()
        start_date_text = self.start_date.text.strip()
        end_date_text = self.end_date.text.strip()

        if self.ref_radio.active and not self.reference_input.text:
            self.show_popup("Error", "Por favor, ingrese una referencia.")
            return

        if self.date_radio.active:
            try:
                start_date = start_date_text
                end_date = end_date_text
                if not start_date or not end_date:
                    raise ValueError
            except ValueError:
                self.show_popup("Error", "Las fechas ingresadas no son válidas.")
                return

            # Filtrar por rango de fechas
            filtered_data = [item for item in self.manager.data if start_date <= item[2] <= end_date]
            if not filtered_data:
                self.show_popup("Aviso", "No se encontraron resultados.")
                return

            self.show_results(filtered_data)
            return

        # Buscar por referencia
        filtered_data = [item for item in self.manager.data if item[0] == reference]
        if not filtered_data:
            self.show_popup("No encontrado", "La referencia no existe en la base de datos.")
            return

        self.show_results(filtered_data)

    def show_results(self, data):
        """ Muestra los resultados de búsqueda en la pantalla de resultados """
        results_screen = self.manager.get_screen("results")
        results_screen.load_data(data)
        self.manager.current = "results"

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()


class MainApp(App):
    """ Contenedor principal con ScreenManager para manejar las pantallas """

    def build(self):
        self.data = [
            ("ALMI25-00163", "VILLARREAL DIVISION", "01/02/2024"),
            ("ALMI24-01936", "LEVARE SISTEMAS", "15/03/2024"),
            ("ALMI2A-01689", "K-FLEX DE MEXICO", "20/04/2024"),
            ("ALMI24-02092", "VILLARREAL DIVISION", "05/05/2024"),
            ("ALMI25-00030", "ACERO PRIME", "12/06/2024"),
            ("ALMI25-00031", "ACERO PRIME remix", "12/06/2024"),
            ("ALMI24-02054", "COMERCIALIZADORA GARTREND", "18/07/2024"),
            ("ALMI24-02099", "PROTEINA ANIMAL", "22/08/2024"),
            ("ALMI24-02084", "OPP FILM MEXICO", "30/09/2024")
        ]

        sm = ScreenManager()
        sm.data = self.data
        sm.add_widget(SearchScreen(name="search"))
        sm.add_widget(PedimentosTable(name="results"))  # Resultados de búsqueda

        return sm


if __name__ == "__main__":
    MainApp().run()
