# models/zes.py

class ZES:
    def __init__(self):
        self.residents = []  # Список всех жильцов

    def add_new_resident(self, resident):
        """Добавление нового жильца в ЖЭС."""
        self.residents.append(resident)

    def calculate_total_services_cost(self):
        """Расчет общей стоимости всех услуг для всех жильцов."""
        total_cost = 0
        for resident in self.residents:
            for service in resident.services:
                total_cost += resident.calculate_service_cost(service['cost'])
        return total_cost

    def save_to_file(self, filename="residents_data.txt"):
        """Сохранение данных о жильцах в текстовый файл."""
        with open(filename, "w", encoding="utf-8") as file:
            for resident in self.residents:
                file.write(f"{resident}\n")
                file.write("Услуги:\n")
                for service in resident.services:
                    file.write(f"  - {service['name']}: {service['cost']} руб.\n")
                file.write("\n")



