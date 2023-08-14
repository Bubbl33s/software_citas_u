import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsBlurEffect
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar la interfaz desde el archivo .ui
        loadUi("ui/main_window.ui", self)

        self.set_fw_highlight()
        # Conectar el botón btn_edit al método toggle_float_window
        self.btn_edit.clicked.connect(self.toggle_float_window)
        self.adjust_table_widget()

# WIDGETS SETTER AND SIZING METHODS---------------------------------------------------------------------------------------
    def set_fw_highlight(self):
        self.float_window.setParent(self.main_container)
        # Inicializar el efecto de desenfoque
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(0)  # Sin desenfoque al inicio
        self.container.setGraphicsEffect(self.blur_effect)
        # Inicializar el overlay para bloquear interacciones y oscurecer
        # Colocado en main_container
        self.overlay = QLabel(self.main_container)
        self.overlay.setGeometry(
            0, 0, self.main_container.width(), self.main_container.height())

        self.overlay.setStyleSheet(
            "background-color: rgba(0, 0, 0, 40); border-radius: 20px;")
        self.overlay.hide()
        self.float_window.hide()

    def resize_float_window(self):
        # Ajustar el tamaño y posición de float_window para que esté centrado
        width_float_window = 800
        height_float_window = 600
        x_float_window = (self.main_container.width() - width_float_window) / 2
        y_float_window = (self.main_container.height() -
                          height_float_window) / 2
        self.float_window.setGeometry(
            int(x_float_window), int(y_float_window), width_float_window, height_float_window)

    def resize_containers(self):
        # Ajustar el tamaño y posición del main_container
        self.main_container_margin = 20
        self.main_container.setGeometry(
            self.main_container_margin, self.main_container_margin,
            self.width() - 2*self.main_container_margin,
            self.height() - 2*self.main_container_margin)

        # Ajustar el tamaño y posición de container para que se mantenga proporcional
        # Margen a 0 para que se puedan poner los widgets al borde
        self.container.setGeometry(
            0, 0, self.main_container.width(), self.main_container.height())

    def resize_buttons(self):
        # Ajustar posición de btn_edit basándose en las proporciones iniciales
        x_btn = self.width() * self.prop_x_btn
        y_btn = self.height() * self.prop_y_btn
        self.btn_edit.move(int(x_btn), int(y_btn))
        # TODO: ADD MORE BUTTONS

    def get_buttons_prop(self):
        # Guardar las proporciones iniciales del botón btn_edit
        self.prop_x_btn = self.btn_edit.x() / self.width()
        self.prop_y_btn = self.btn_edit.y() / self.height()
        # TODO: ADD MORE BUTTONS

    def resizeEvent(self, event):
        self.resize_containers()
        self.resize_float_window()

        # Ajustar el tamaño del overlay
        self.overlay.setGeometry(0, 0, self.main_container.width(),
                                 self.main_container.height())

        self.adjust_table_widget()

    def adjust_table_widget(self):
        self.table_margin = 20  # Margen uniforme (lateral, inferior)
        self.table_top_offset = 200  # Separación desde la parte superior

        table_width = self.container.width() - 2 * self.table_margin
        table_height = self.container.height() - self.table_top_offset - \
            self.table_margin

        # Cálculo para centrar horizontalmente
        table_x_position = int((self.container.width() - table_width) / 2)

        self.tbl_appoinment.setGeometry(
            table_x_position, self.table_top_offset, table_width, table_height)

    def toggle_float_window(self):
        if self.float_window.isVisible():
            self.float_window.hide()
            self.overlay.hide()
            self.blur_effect.setBlurRadius(0)  # Sin desenfoque
        else:
            # Ajusta el nivel de desenfoque según prefieras
            self.blur_effect.setBlurRadius(10)

            width_float_window = 800
            height_float_window = 600
            x_float_window = (self.main_container.width() -
                              width_float_window) / 2
            y_float_window = (self.main_container.height() -
                              height_float_window) / 2
            self.float_window.setGeometry(
                int(x_float_window), int(y_float_window), width_float_window, height_float_window)

            self.float_window.show()
            self.overlay.show()
            self.overlay.raise_()  # Asegurar que overlay esté por debajo de float_window
            self.float_window.raise_()  # Asegurar que float_window esté encima
# ------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = VentanaPrincipal()
    main_win.show()
    sys.exit(app.exec_())
