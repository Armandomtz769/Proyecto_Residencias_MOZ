import sys
from PySide6.QtCore import Qt, QDate # type: ignore
from PySide6.QtGui import QFont # type: ignore
from PySide6.QtWidgets import ( # type: ignore
    QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, 
    QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, 
    QSizePolicy, QStackedWidget, QLineEdit, QCalendarWidget, 
    QRadioButton, QFrame, QButtonGroup, QMessageBox
)

class PedimentosTable(QWidget):
    """ Pantalla de la tabla de Pedimentos """
    def __init__(self, stacked_widget, data):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()

        # Barra superior con botón de regreso
        header_layout = QHBoxLayout()
        back_button = QPushButton("←")
        back_button.setFixedSize(40, 40)
        back_button.clicked.connect(self.go_back)

        title_label = QLabel("Resultados de Búsqueda")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        header_layout.addWidget(back_button)
        header_layout.addStretch(1)
        header_layout.addWidget(title_label)
        header_layout.addStretch(1)

        layout.addLayout(header_layout)

        # Tabla de Pedimentos
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Número de Referencia", "Empresa", "Fecha"])
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)

        self.table.setRowCount(len(data))
        font_big = QFont("Arial", 12, QFont.Bold)
        font_small = QFont("Arial", 10)

        for row, (pedimento, empresa, fecha) in enumerate(data):
            item_pedimento = QTableWidgetItem(pedimento)
            item_pedimento.setFont(font_big)

            item_empresa = QTableWidgetItem(empresa)
            item_empresa.setFont(font_small)

            item_fecha = QTableWidgetItem(fecha)
            item_fecha.setFont(font_small)

            self.table.setItem(row, 0, item_pedimento)
            self.table.setItem(row, 1, item_empresa)
            self.table.setItem(row, 2, item_fecha)

        layout.addWidget(self.table)
        self.setLayout(layout)

    def go_back(self):
        """ Regresa a la pantalla de búsqueda """
        self.stacked_widget.setCurrentIndex(0)
