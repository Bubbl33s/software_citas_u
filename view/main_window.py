import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

from controller.load_from_json import get_appointments_list


class MainUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar la interfaz desde el archivo .ui
        loadUi("ui/main_window.ui", self)

        # LLENAR LA TABLA
        self.appointments_list = get_appointments_list()
        self.fill_table(self.appointments_list)

        self.set_fw_highlight()
        # Conectar el botón btn_edit al método toggle_float_window
        self.btn_edit.clicked.connect(self.toggle_float_window)

        self.resize_table_widget()
        self.set_table()

        total_initial_width = self.tbl_appointment.width()
        self.column_proportions = [self.tbl_appointment.columnWidth(i) / total_initial_width
                                   for i in range(self.tbl_appointment.columnCount())]
        # Proporción de las columnas de la tabla

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

        self.resize_table_widget()
        self.resize_table_columns_width()

    def resize_table_widget(self):
        self.table_margin = 20  # Margen uniforme (lateral, inferior)
        self.table_top_offset = 200  # Separación desde la parte superior

        table_width = self.container.width() - 2 * self.table_margin
        table_height = self.container.height() - self.table_top_offset - \
            self.table_margin

        # Cálculo para centrar horizontalmente
        table_x_position = int((self.container.width() - table_width) / 2)

        self.tbl_appointment.setGeometry(
            table_x_position, self.table_top_offset, table_width, table_height)

    def resize_table_columns_width(self):
        for index, proportion in enumerate(self.column_proportions):
            self.tbl_appointment.setColumnWidth(
                index, int(self.tbl_appointment.width() * proportion))

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
            x_float_window = int((self.main_container.width() -
                                  width_float_window) / 2)
            y_float_window = int((self.main_container.height() -
                                  height_float_window) / 2)
            self.float_window.setGeometry(
                x_float_window, y_float_window, width_float_window, height_float_window)

            self.float_window.show()
            self.overlay.show()
            self.overlay.raise_()  # Asegurar que overlay esté por debajo de float_window
            self.float_window.raise_()  # Asegurar que float_window esté encima
# ------------------------------------------------------------------------------------------------------------------------
    """
    ID CITA, FECHA PROG, HORA PROG AP PAT, AP MAT, NOMBRES, CÓDIGO, CONCEPTO, OBS, FLAG, ESTADO, TELÉFONO, CORREO, FECHA DE REGISTRO, HORA DE REGISTRO
    MOSTRAR: ID CITA, FECHA PROG, HORA PROG, AP PAT, AP MAT, NOMBRES, CÓDIGO, CONCEPTO, FLAG, ESTADO
    """

    def set_table(self):
        self.tbl_appointment.verticalHeader().setFixedWidth(32)
        self.tbl_appointment.verticalHeader().setDefaultAlignment(
            Qt.AlignRight | Qt.AlignVCenter)
        self.tbl_appointment.horizontalHeader().setFixedHeight(40)
        self.tbl_appointment.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tbl_appointment.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def fill_table(self, lists_to_fill):
        for single_list in lists_to_fill:
            row_pos = self.tbl_appointment.rowCount()
            self.tbl_appointment.insertRow(row_pos)

            for i, value in enumerate(single_list):
                self.tbl_appointment.setItem(
                    row_pos, i, QTableWidgetItem(value))
