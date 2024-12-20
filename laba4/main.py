import sys
import os

# Добавляем путь до корневой папки проекта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main_window import MainWindow

if __name__ == "__main__":
    MainWindow()