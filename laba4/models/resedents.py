# models/residents.py

class RegularResident:
    def __init__(self, name, apartment):
        self.name = name
        self.apartment = apartment

    def to_dict(self):
        return {"type": "Обычный", "name": self.name, "apartment": self.apartment}

    def __repr__(self):
        return f"RegularResident(name={self.name}, apartment={self.apartment})"


class PrivilegedResident(RegularResident):
    def __init__(self, name, apartment):
        super().__init__(name, apartment)

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Льготный"
        return data

    def __repr__(self):
        return f"PrivilegedResident(name={self.name}, apartment={self.apartment})"
