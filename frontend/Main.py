import sys
from PySide6.QtCore import Qt, QDate # type: ignore
from PySide6.QtGui import QFont # type: ignore
from PySide6.QtWidgets import ( # type: ignore
    QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, 
    QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, 
    QSizePolicy, QStackedWidget, QLineEdit, QCalendarWidget, 
    QRadioButton, QFrame, QButtonGroup, QMessageBox
)
from ShipmentsList import PedimentosTable
from ShipmentDetails import ReferenceDetails
class SearchApp(QWidget):
    """ Pantalla de búsqueda de pedimentos """
    def __init__(self, stacked_widget, data):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.data = data  # Datos de pedimentos
        self.setWindowTitle("Búsqueda de Pedimentos")

        layout = QVBoxLayout()

        # Búsqueda por Fecha
        self.date_frame = QFrame()
        date_layout = QVBoxLayout()

        self.date_radio = QRadioButton("Búsqueda por fecha")
        self.date_radio.setChecked(True)
        self.date_radio.toggled.connect(self.toggle_calendar)
        date_layout.addWidget(self.date_radio)

        self.start_date = QLineEdit()
        self.start_date.setPlaceholderText("Inicio: dd/mm/aaaa")
        date_layout.addWidget(self.start_date)

        self.end_date = QLineEdit()
        self.end_date.setPlaceholderText("Fin: dd/mm/aaaa")
        date_layout.addWidget(self.end_date)

        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.set_date)
        date_layout.addWidget(self.calendar)

        self.date_frame.setLayout(date_layout)
        layout.addWidget(self.date_frame)

        # Búsqueda por Referencia
        self.ref_frame = QFrame()
        ref_layout = QVBoxLayout()

        self.ref_radio = QRadioButton("Búsqueda por referencia")
        ref_layout.addWidget(self.ref_radio)

        self.reference_input = QLineEdit()
        self.reference_input.setPlaceholderText("Referencia: ALMI24-00000")
        ref_layout.addWidget(self.reference_input)

        self.ref_frame.setLayout(ref_layout)
        layout.addWidget(self.ref_frame)

        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.date_radio)
        self.radio_group.addButton(self.ref_radio)

        # Botón de búsqueda
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search_reference)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

    def toggle_calendar(self):
        """ Muestra u oculta el calendario según la opción elegida """
        self.calendar.setVisible(self.date_radio.isChecked())

    def set_date(self, date):
        """ Asigna la fecha seleccionada en los campos de texto """
        if not self.start_date.text():
            self.start_date.setText(date.toString("dd/MM/yyyy"))
        else:
            self.end_date.setText(date.toString("dd/MM/yyyy"))

    def search_reference(self):
        """ Busca la referencia o rango de fechas ingresado y muestra los resultados """
        reference = "ALMI"+self.reference_input.text().strip().upper()
        start_date_text = self.start_date.text().strip()
        end_date_text = self.end_date.text().strip()

        if self.ref_radio.isChecked() and not reference:
            QMessageBox.warning(self, "Error", "Por favor, ingrese una referencia.")
            return

        if self.date_radio.isChecked():
            # Verificar que las fechas sean válidas
            try:
                start_date = QDate.fromString(start_date_text, "dd/MM/yyyy")
                end_date = QDate.fromString(end_date_text, "dd/MM/yyyy")
                if not start_date.isValid() or not end_date.isValid():
                    raise ValueError
            except ValueError:
                QMessageBox.warning(self, "Error", "Las fechas ingresadas no son válidas.")
                return

##UIMPORTANTE REVISAR QUE MEJOR SE M<ANDE UN MENSAJE DE QUE  NO ENCONTRO FECHAS CUANDO NO HAY RESULTADOS
            # Filtrar por rango de fechas
            filtered_data = [item for item in self.data if start_date <= QDate.fromString(item[2], "dd/MM/yyyy") <= end_date]
            self.show_results(filtered_data)
            return

        # Buscar la referencia
        filtered_data = [item for item in self.data if item[0] == reference]
        if not filtered_data:
            QMessageBox.warning(self, "No encontrado", "La referencia no existe en la base de datos.")
            return

        self.show_results(filtered_data)

    def show_results(self, data):
        """ Muestra los resultados de búsqueda en la pantalla de resultados """
        self.results_screen = PedimentosTable(self.stacked_widget, data)
        self.stacked_widget.addWidget(self.results_screen)
        self.stacked_widget.setCurrentWidget(self.results_screen)

class MainApp(QWidget):
    """ Contenedor principal con QStackedWidget para manejar las pantallas """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Pedimentos")
        self.setGeometry(100, 100, 400, 600)
        self.setFixedSize(400, 600)

        layout = QVBoxLayout()

        # Datos de ejemplo
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

        self.stacked_widget = QStackedWidget()
        self.search_screen = SearchApp(self.stacked_widget, self.data)
        # self.results_screen = PedimentosTable(self.stacked_widget, self.data)

        self.stacked_widget.addWidget(self.search_screen)
        # self.stacked_widget.addWidget(self.results_screen)

        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()