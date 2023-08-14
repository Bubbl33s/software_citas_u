import sys
from PyQt5.QtWidgets import QApplication
from view.main_window import MainUserWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainUserWindow()
    main_win.show()
    sys.exit(app.exec_())
