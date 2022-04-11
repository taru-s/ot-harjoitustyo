from entities.fabric import Fabric
from initialize_database import initialize_database
from database_connection import get_database_connection


# class FabricRepository:
#     def __init__(self) -> None:
#         self._fabrics = {}

#     def add_fabric(self, fabric:Fabric):
#         self._fabrics[fabric.name] = fabric

#     def get_all_fabrics(self):
#         return [str(f) for f in self._fabrics.values()]

#     def get_fabric_by_name(self, name):
#         if name in self._fabrics:
#             return self._fabrics[name]
#         return False


def get_fabric_by_row(row):
    return Fabric(row['name'], row['width'], row['length'], row['washed']) if row else None

class FabricRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all_fabrics(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from Fabrics")
        rows = cursor.fetchall()

        return [str(Fabric(row["name"], row["width"], row["length"], row["washed"])) for row in rows]

    def get_fabric_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics WHERE name = ?", [name])
        row = cursor.fetchone()

        return get_fabric_by_row(row)


    def add_fabric(self, fabric:Fabric):
        cursor = self._connection.cursor()
        values = fabric.get_values()
        cursor.execute("INSERT INTO Fabrics (name, width, length, washed) VALUES (?,?,?,?)", values)
        self._connection.commit()

fabric_repository = FabricRepository(get_database_connection())
# fabric_repository.add_fabric(Fabric("testi", 100, 200, 0))
# print(fabric_repository.get_all_fabrics())