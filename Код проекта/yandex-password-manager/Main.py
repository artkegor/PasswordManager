import sys

from PyQt5.QtWidgets import QApplication

from Database import conn
from ui.MainWindow import MainWindow

# Основной скрипт, запускающий рабочую программу
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow().show()

    ret = app.exec()
    conn.close()
    sys.exit(ret)
