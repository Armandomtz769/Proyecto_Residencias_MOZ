from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ReferenceDetails(Screen):
    """ Pantalla para mostrar detalles de un pedimento """

    def __init__(self, referencia="", empresa="", fecha="", **kwargs):
        super().__init__(**kwargs)
        self.referencia = referencia
        self.empresa = empresa
        self.fecha = fecha

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.title_label = Label(text=f"Referencia: {self.referencia}", font_size=18, bold=True)
        self.empresa_label = Label(text=f"Empresa: {self.empresa}", font_size=16)
        self.fecha_label = Label(text=f"Fecha: {self.fecha}", font_size=16)

        layout.add_widget(self.title_label)
        layout.add_widget(self.empresa_label)
        layout.add_widget(self.fecha_label)

        # Botón para regresar
        self.back_button = Button(text="Volver", size_hint=(1, 0.2))
        self.back_button.bind(on_press=self.go_back)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def load_details(self, referencia, empresa, fecha):
        """ Carga los detalles en la pantalla """
        self.referencia = referencia
        self.empresa = empresa
        self.fecha = fecha
        self.title_label.text = f"Referencia: {self.referencia}"
        self.empresa_label.text = f"Empresa: {self.empresa}"
        self.fecha_label.text = f"Fecha: {self.fecha}"

    def go_back(self, instance):
        """ Regresa a la pantalla anterior """
        self.manager.current = "results"  # Regresa a la pantalla de resultados
