import os

from dotenv import load_dotenv

# Имя пользователя и пароль от базы данных, хранится в .env
load_dotenv()
USER_NAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
