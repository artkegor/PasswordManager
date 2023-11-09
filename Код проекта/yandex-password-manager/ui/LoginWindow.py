from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, \
    QLineEdit, QMessageBox, QGridLayout

import Database
from Database import create_app_account, login
from ui.widget.CenterWidget import CenterWidget


# Класс входа в аккаунт менеджера паролей
class LoginWindow(QWidget, CenterWidget):
    def __init__(self, mv):
        super().__init__()
        self.mv = mv
        self.setWindowTitle('Авторизоваться')
        self.account = QLineEdit()
        self.password = QLineEdit()
        self.init_ui()
        self.setGeometry(300, 150, 300, 150)
        self.center()

    def init_ui(self):

        grid = QGridLayout()
        grid.setSpacing(15)
        grid.addWidget(QLabel('Имя пользователя'), 1, 0)
        grid.addWidget(self.account, 1, 1)

        grid.addWidget(QLabel('Пароль'), 2, 0)
        grid.addWidget(self.password, 2, 1)

        hbox_btn = QHBoxLayout()
        hbox_btn.setSpacing(5)

        need_register = Database.exist_app_account()
        if need_register:
            register_btn = QPushButton("Зарегестрироваться")
            register_btn.clicked.connect(self.do_register)
            hbox_btn.addWidget(register_btn)
        else:
            confirm_btn = QPushButton("Авторизоваться")
            confirm_btn.clicked.connect(self.do_login)
            hbox_btn.addWidget(confirm_btn)

        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(self.quit)
        hbox_btn.addWidget(close_btn)
        btns = QWidget()
        btns.setLayout(hbox_btn)
        grid.addWidget(btns, 3, 0, 1, 2)

        self.setLayout(grid)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def do_login(self):
        account = self.account.text()
        password = self.password.text()
        if login(account, password):
            self.open_main_window()
        else:
            QMessageBox.warning(self, 'Неверное имя учетной записи или пароль',
                                'Неверное имя учетной записи или пароль.')

    def do_register(self):
        account = self.account.text()
        password = self.password.text()
        if create_app_account(account, password):
            QMessageBox.information(self, 'Вы успешно зарегистрировались',
                                    'Регистрация прошла успешно, приветствую' + account)
            self.open_main_window()

    def open_main_window(self):
        self.close()
        self.mv.init_signal.emit()
        self.mv.init_ui()

    def quit(self):
        self.close()
        self.mv.quit_signal.emit()
