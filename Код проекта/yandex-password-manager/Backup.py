import os
import pickle
from datetime import datetime

from Common import backup_dir


# Вспомогательный скрипт, реализующий бэкенд создания и загрузки резервных копий
def backup(accounts):
    file = backup_dir.joinpath(datetime.now().strftime('%Y%m%d%H%M%S') + '.bin')
    pickle.dump(accounts, open(file, "wb"))
    return file


def list_backups():
    return os.listdir(backup_dir)


def load_backup(file):
    return pickle.load(open(file, "rb"))
