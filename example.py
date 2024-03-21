from dataclasses import dataclass
from MazgaDB import MazgaDB

@dataclass
class People:
    id: int
    fname: str

"""
Пример с работай с базай данных
"""
db = MazgaDB("users.db", {"users": People})

db.create_table("users", {"id": "INT", "fname": "TEXT"})

print(db.read_table("users"))

db.append_line("users", [1, "Mazga"])

print(db.read_table("users"))

db.update_line("users", key1="id", value1="1", key2="fname", value2="Mazga2")

print(db.read_table("users"))

db.delete_line("users", key="id", value=1)

print(db.read_table("users"))

db.append_column("users", "lname", "TEXT")

print(db.read_table("users"))

db.delete_column("users", "lname")

print(db.read_table("users"))

db.select("users", key="id", value="1")

print(db.read_table("users"))

db.append_line("users", [1, "Mazga"])

print(db.select_class("users", key="id", value="1", class_data=People))

print(db.read_table("users"))

print(db.read_table("users"))

print(db.saw_tables())

print(db.execute("SELECT * FROM users"))
"GOOD"
