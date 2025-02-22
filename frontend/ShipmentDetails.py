import sys
from PySide6.QtCore import Qt, QDate # type: ignore
from PySide6.QtGui import QFont # type: ignore
from PySide6.QtWidgets import ( # type: ignore
    QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, 
    QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, 
    QSizePolicy, QStackedWidget, QLineEdit, QCalendarWidget, 
    QRadioButton, QFrame, QButtonGroup, QMessageBox
)


class ReferenceDetails(QWidget):
    """ Ventana externa para mostrar detalles de un pedimento """
    def __init__(self, referencia, empresa, fecha):
        super().__init__()
        self.setWindowTitle(f"Detalles - {referencia}")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        title_label = QLabel(f"Referencia: {referencia}")
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        empresa_label = QLabel(f"Empresa: {empresa}")
        empresa_label.setFont(QFont("Arial", 12))
        empresa_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        fecha_label = QLabel(f"Fecha: {fecha}")
        fecha_label.setFont(QFont("Arial", 12))
        fecha_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)
        layout.addWidget(empresa_label)
        layout.addWidget(fecha_label)

        self.setLayout(layout)
