import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Добавляем путь до корневой папки проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.database import database  # Импортируем экземпляр database

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Главное окно")
        self.db = database  # Используем импортированный экземпляр database
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Создание виджетов главного окна
        pass

    # Другие методы класса MainWindow