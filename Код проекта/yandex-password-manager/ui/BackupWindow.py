from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QAbstractItemView

import Backup
import Database
from Common import backup_dir
from ui.widget.CenterWidget import CenterWidget


# Класс окна для загрузки ранее созданных в приложении резервных копий
class LoadBackupWindow(QWidget, CenterWidget):
    def __init__(self, refresh_signal):
        super(LoadBackupWindow, self).__init__()
        self.refresh_signal = refresh_signal

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.addWidget(QLabel('Выберите файл резервной копии для загрузки: '))

        self.backups_listview = QListView()
        self.backups_listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.backups_listview.setSpacing(5)
        self.backups_listview.clicked.connect(self.choose_backup)
        layout.addWidget(self.backups_listview)

        self.setLayout(layout)
        self.center()

    def choose_backup(self, idx):
        file = self.backups[idx.row()]
        file = backup_dir.joinpath(file)
        accounts = Backup.load_backup(file)
        Database.restore_accounts(accounts)
        self.refresh_signal.emit()
        self.close()

    def load_backups(self):
        self.backups = Backup.list_backups()
        slm = QStringListModel()
        slm.setStringList(self.backups)
        self.backups_listview.setModel(slm)
