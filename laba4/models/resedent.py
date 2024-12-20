from abc import ABC, abstractmethod

class Resident(ABC):
    def __init__(self, name, apartment):
        self.name = name
        self.apartment = apartment
        self.services = []

    def add_service(self, name, cost):
        self.services.append({'name': name, 'cost': cost})

    @abstractmethod
    def calculate_total_cost(self):
        pass

class RegularResident(Resident):
    def calculate_total_cost(self):
        return sum(service['cost'] for service in self.services)

class PrivilegedResident(Resident):
    def calculate_total_cost(self):
        # Предположим, что льготные жильцы получают 50% скидку
        return sum(service['cost'] for service in self.services) * 0.5