import os
from pathlib import Path

from dotenv import load_dotenv

# Имя пользователя и пароль от базы данных, хранится в .env
load_dotenv()
USER_NAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

# Папки
ROOT = Path(__file__).resolve().parent
NORTH_DATA = Path(ROOT, 'homework-1', 'north_data')
