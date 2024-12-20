import os

print("Текущая рабочая директория:", os.getcwd())
print("Содержимое текущей директории:", os.listdir())
print("Содержимое родительской директории:", os.listdir('..'))
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Добавляем корневую директорию проекта в sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from models.resedents import RegularResident, PrivilegedResident
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("Текущий sys.path:", sys.path)
    print("Содержимое директории models:")
    models_dir = os.path.join(project_root, 'models')
    print(os.listdir(models_dir))
    raise

class ResidentWindow:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db

        self.window = tk.Toplevel(parent)
        self.window.title("Добавить Жильца")
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.window, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        self.name_entry = ttk.Entry(frame)
        self.name_entry.insert(0, "Имя жильца")
        self.name_entry.pack(pady=5)

        self.apartment_entry = ttk.Entry(frame)
        self.apartment_entry.insert(0, "Номер квартиры")
        self.apartment_entry.pack(pady=5)

        self.resident_type_combo = ttk.Combobox(frame, values=["Обычный", "Льготный"])
        self.resident_type_combo.set("Обычный")
        self.resident_type_combo.pack(pady=5)

        ttk.Button(frame, text="Сохранить", command=self.save_resident).pack(pady=10)

    def save_resident(self):
        name = self.name_entry.get()
        try:
            apartment = int(self.apartment_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Номер квартиры должен быть числом")
            return

        res_type = self.resident_type_combo.get()

        if res_type == "Обычный":
            resident = RegularResident(name, apartment)
        elif res_type == "Льготный":
            resident = PrivilegedResident(name, apartment)
        else:
            messagebox.showerror("Ошибка", "Выберите тип жильца")
            return

        try:
            self.db.add_resident(resident)
            messagebox.showinfo("Успех", "Жилец добавлен!")
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить жильца: {str(e)}")