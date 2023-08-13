import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsBlurEffect
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar la interfaz desde el archivo .ui
        loadUi("ui/main_window.ui", self)

        # Conectar el botón btn_edit al método toggle_float_window
        self.btn_edit.clicked.connect(self.toggle_float_window)

        # Guardar las proporciones iniciales del botón btn_edit
        self.proporcion_x_btn = self.btn_edit.x() / self.width()
        self.proporcion_y_btn = self.btn_edit.y() / self.height()

        # Inicializar el efecto de desenfoque
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(0)  # Sin desenfoque al inicio
        self.container.setGraphicsEffect(self.blur_effect)

        # Inicializar el overlay para bloquear interacciones y oscurecer
        # Colocado en main_container
        self.overlay = QLabel(self.main_container)
        self.overlay.setGeometry(
            0, 0, self.main_container.width(), self.main_container.height())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 40);")
        self.overlay.hide()
        self.float_window.hide()

    def resizeEvent(self, event):  # <-- Asegúrate de que 'E' esté en mayúsculas
        # Ajustar el tamaño y posición del main_container
        margin = 20
        self.main_container.setGeometry(
            margin, margin, self.width() - 2*margin, self.height() - 2*margin)

        # Ajustar el tamaño y posición de container para que se mantenga proporcional
        margin_container = 20
        self.container.setGeometry(
            margin_container, margin_container,
            self.main_container.width() - 2*margin_container,
            self.main_container.height() - 2*margin_container)

        # Ajustar el tamaño y posición de float_window
        ancho_float_window = 800
        alto_float_window = 600
        x_float_window = int(
            (self.main_container.width() - ancho_float_window) / 2)
        y_float_window = int(
            (self.main_container.height() - alto_float_window) / 2)
        self.float_window.setGeometry(
            x_float_window, y_float_window, ancho_float_window, alto_float_window)

        # Ajustar posición de btn_edit basándose en las proporciones iniciales
        x_btn = self.width() * self.proporcion_x_btn
        y_btn = self.height() * self.proporcion_y_btn
        self.btn_edit.move(int(x_btn), int(y_btn))

        # Ajustar el tamaño del overlay
        self.overlay.setGeometry(0, 0, self.main_container.width(),
                                 self.main_container.height())

    def toggle_float_window(self):
        if self.float_window.isVisible():
            self.float_window.hide()
            self.overlay.hide()
            self.blur_effect.setBlurRadius(0)  # Sin desenfoque
        else:
            self.float_window.show()
            self.overlay.show()
            self.overlay.raise_()  # Asegurar que overlay esté por debajo de float_window
            self.float_window.raise_()  # Asegurar que float_window esté encima
            # Ajusta el nivel de desenfoque según prefieras
            self.blur_effect.setBlurRadius(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = VentanaPrincipal()
    main_win.show()
    sys.exit(app.exec_())
