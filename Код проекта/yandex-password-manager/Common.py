import os
import pathlib

# Вспомогательный скрипт
db_path = pathlib.Path(__file__).parent.joinpath('pm.db').absolute()

backup_dir = pathlib.Path(__file__).parent.joinpath('backup').absolute()

ACCOUNT_ID = 0
ACCOUNT_NAME = 1
USERNAME = 2
PASSWORD = 3
USED_BY = 4
DATE = 5

PASSWORD_MASK = '******'

if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)
