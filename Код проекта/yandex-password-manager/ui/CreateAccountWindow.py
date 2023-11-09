from datetime import datetime

from PyQt5.QtWidgets import QWidget

import Cryptor
import Database
from ui.widget.AccountWidget import AccountWidget
from ui.widget.CenterWidget import CenterWidget


# Класс окна создания нового пароля
class CreateAccountWindow(QWidget, CenterWidget):
    def __init__(self, mv):
        super().__init__()
        self.mv = mv
        self.setWindowTitle('Добавление пароля')
        self.account_widget = AccountWidget()
        self.account_widget.confirm_btn.clicked.connect(self.create_account)
        self.account_widget.cancel_btn.clicked.connect(self.close)
        self.setLayout(self.account_widget.layout)
        self.setGeometry(400, 200, 400, 200)
        self.center()

    def create_account(self):
        an, un, pw, ub = self.account_widget.get_account_info()
        pw = Cryptor.encode(pw)
        if Database.insert_account(an, un, pw, ub,
                                   datetime.now().date()):
            self.account_widget.msg.setText('Успешно добавлен пароль')
            self.mv.refresh_data_signal.emit()
        else:
            self.account_widget.msg.setText('Пароль от этого ресурса уже создан')
