class ResidentType:
    def __init__(self, name, apartment):
        self.name = name
        self.apartment = apartment

class RegularResident(ResidentType):
    def __str__(self):
        return f"Обычный жилец: {self.name}, Квартира: {self.apartment}"

class PrivilegedResident(ResidentType):
    def __str__(self):
        return f"Льготный жилец: {self.name}, Квартира: {self.apartment}"