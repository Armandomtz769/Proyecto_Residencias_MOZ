from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QCalendarWidget,
    QRadioButton, QLabel, QHBoxLayout, QFrame, QButtonGroup
)
from PySide6.QtGui import QPalette, QColor
import sys

class SearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Búsqueda de Pedimentos")
        self.setGeometry(100, 100, 300, 400)

        # Establecer colores de fondo y texto
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(242, 242, 242))  # Gris claro
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))  # Texto negro
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Búsqueda por Fecha
        self.date_frame = QFrame()
        date_layout = QVBoxLayout()

        self.date_radio = QRadioButton("Búsqueda por fecha")
        self.date_radio.setChecked(True)
        self.date_radio.toggled.connect(self.toggle_calendar)
        self.date_radio.setStyleSheet("color: black;")
        date_layout.addWidget(self.date_radio)

        self.start_date = QLineEdit()
        self.start_date.setPlaceholderText("Inicio: dd/mm/aaaa")
        self.start_date.setStyleSheet("background: transparent; border: 2px solid blue; color: black;")
        date_layout.addWidget(self.start_date)

        self.end_date = QLineEdit()
        self.end_date.setPlaceholderText("Fin: dd/mm/aaaa")
        self.end_date.setStyleSheet("background: transparent; border: 2px solid blue; color: black;")
        date_layout.addWidget(self.end_date)

        self.calendar = QCalendarWidget()
        self.calendar.hide()
        self.calendar.clicked.connect(self.set_date)
        date_layout.addWidget(self.calendar)

        self.date_frame.setLayout(date_layout)
        layout.addWidget(self.date_frame)

        # Búsqueda por Referencia
        self.ref_frame = QFrame()
        ref_layout = QVBoxLayout()

        self.ref_radio = QRadioButton("Búsqueda por referencia")
        self.ref_radio.setStyleSheet("color: black;")
        ref_layout.addWidget(self.ref_radio)

        self.reference_input = QLineEdit()
        self.reference_input.setPlaceholderText("Referencia: ALMI24-00000")
        self.reference_input.setStyleSheet("background: transparent; border: 2px solid blue; color: black;")
        ref_layout.addWidget(self.reference_input)

        self.ref_frame.setLayout(ref_layout)
        layout.addWidget(self.ref_frame)

        # Grupo de botones para exclusividad
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.date_radio)
        self.radio_group.addButton(self.ref_radio)

        # Botón de búsqueda
        self.search_button = QPushButton("Buscar")
        self.search_button.setStyleSheet("color: black;")
        layout.addWidget(self.search_button)

        self.setLayout(layout)

    def toggle_calendar(self):
        if self.date_radio.isChecked():
            self.calendar.show()
        else:
            self.calendar.hide()

    def set_date(self, date):
        if not self.start_date.text():
            self.start_date.setText(date.toString("dd/mm/aaaa"))
        else:
            self.end_date.setText(date.toString("dd/mm/aaaa"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchApp()
    window.show()
    sys.exit(app.exec())