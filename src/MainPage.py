from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QComboBox, 
    QRadioButton, QLabel, QHBoxLayout, QFrame, QButtonGroup
)
import sys

class MiApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Búsqueda de Pedimentos")
        self.setGeometry(100, 100, 360, 640)  # Tamaño optimizado para móviles

        layout_principal = QVBoxLayout()

        # Grupo de botones de radio para que solo se pueda seleccionar uno
        self.radio_group = QButtonGroup()

        # Sección: Buscar por Rango de Fechas
        self.fecha_widget = QFrame()
        self.fecha_widget.setStyleSheet("background-color: #0D47A1; border: 2px solid #0B3D91; border-radius: 10px; padding: 10px;")
        layout_fecha = QVBoxLayout()
        
        titulo_fecha = QLabel("Búsqueda por Fechas")
        titulo_fecha.setStyleSheet("background-color: #1565C0; color: white; font-weight: bold; padding: 8px; border-radius: 5px; font-size: 16px;")
        layout_fecha.addWidget(titulo_fecha)
        
        fecha_layout = QVBoxLayout()
        self.radio_fecha = QRadioButton()
        self.radio_group.addButton(self.radio_fecha)
        self.radio_fecha.setStyleSheet("font-size: 16px;")
        fecha_layout.addWidget(self.radio_fecha)
        
        fecha_inicio_layout = QHBoxLayout()
        label_inicio = QLabel("Fecha Inicio:")
        label_inicio.setStyleSheet("color: white; font-size: 14px;")
        self.dia_inicio = QComboBox()
        self.mes_inicio = QComboBox()
        self.anio_inicio = QComboBox()
        self.configurar_combo_fechas(self.dia_inicio, self.mes_inicio, self.anio_inicio)
        fecha_inicio_layout.addWidget(label_inicio)
        fecha_inicio_layout.addWidget(self.dia_inicio)
        fecha_inicio_layout.addWidget(self.mes_inicio)
        fecha_inicio_layout.addWidget(self.anio_inicio)
        
        fecha_fin_layout = QHBoxLayout()
        label_fin = QLabel("Fecha Fin:")
        label_fin.setStyleSheet("color: white; font-size: 14px;")
        self.dia_fin = QComboBox()
        self.mes_fin = QComboBox()
        self.anio_fin = QComboBox()
        self.configurar_combo_fechas(self.dia_fin, self.mes_fin, self.anio_fin)
        fecha_fin_layout.addWidget(label_fin)
        fecha_fin_layout.addWidget(self.dia_fin)
        fecha_fin_layout.addWidget(self.mes_fin)
        fecha_fin_layout.addWidget(self.anio_fin)
        
        fecha_layout.addLayout(fecha_inicio_layout)
        fecha_layout.addLayout(fecha_fin_layout)
        layout_fecha.addLayout(fecha_layout)
        self.fecha_widget.setLayout(layout_fecha)
        layout_principal.addWidget(self.fecha_widget, 2)

        # Sección: Buscar por Pedimento
        self.pedimento_widget = QFrame()
        self.pedimento_widget.setStyleSheet("background-color: #1A237E; border: 2px solid #0D1B6A; border-radius: 10px; padding: 10px;")
        layout_pedimento = QVBoxLayout()
        
        titulo_pedimento = QLabel("Búsqueda por Pedimento")
        titulo_pedimento.setStyleSheet("background-color: #283593; color: white; font-weight: bold; padding: 8px; border-radius: 5px; font-size: 16px;")
        layout_pedimento.addWidget(titulo_pedimento)
        
        pedimento_layout = QHBoxLayout()
        self.radio_pedimento = QRadioButton()
        self.radio_group.addButton(self.radio_pedimento)
        self.radio_pedimento.setStyleSheet("font-size: 16px;")
        pedimento_layout.addWidget(self.radio_pedimento)
        
        self.input_pedimento = QLineEdit()
        self.input_pedimento.setPlaceholderText("Ingrese el pedimento")
        self.input_pedimento.setStyleSheet("background-color: white; border-radius: 5px; padding: 5px; font-size: 16px;")
        pedimento_layout.addWidget(self.input_pedimento)
        
        layout_pedimento.addLayout(pedimento_layout)
        self.pedimento_widget.setLayout(layout_pedimento)
        layout_principal.addWidget(self.pedimento_widget, 1)

        # Botón de búsqueda
        self.boton_buscar = QPushButton("Buscar")
        self.boton_buscar.setStyleSheet("font-size: 18px; padding: 12px; background-color: #1565C0; color: white; border-radius: 5px;")
        layout_principal.addWidget(self.boton_buscar)

        self.setLayout(layout_principal)

    def configurar_combo_fechas(self, dia, mes, anio):
        dias = [str(i) for i in range(1, 32)]
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        anios = [str(i) for i in range(2000, 2031)]
        
        dia.addItems(dias)
        mes.addItems(meses)
        anio.addItems(anios)
        
        dia.setStyleSheet("background-color: white; padding: 5px; border-radius: 5px;")
        mes.setStyleSheet("background-color: white; padding: 5px; border-radius: 5px;")
        anio.setStyleSheet("background-color: white; padding: 5px; border-radius: 5px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiApp()
    ventana.show()
    sys.exit(app.exec())
