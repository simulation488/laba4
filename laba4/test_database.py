from models.database import Database

def test_add_resident():
    db = Database()
    db.add_resident({"name": "Тест", "apartment": 101, "type": "Обычный"})
    assert len(db.residents) > 0
