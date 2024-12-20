class Database:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

    # Другие методы класса Database

# Создаем экземпляр базы данных
database = Database()