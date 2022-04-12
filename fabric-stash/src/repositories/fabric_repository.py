from entities.fabric import Fabric


class FabricRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all_fabrics(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics")
        rows = cursor.fetchall()

        return [Fabric(row["name"], row["width"], row["length"],
                       row["washed"]) for row in rows]

    def get_fabric_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics WHERE name = ?", [name])
        rows = cursor.fetchall()

        return [Fabric(row["name"], row["width"], row["length"],
                       row["washed"]) for row in rows]

    def add_fabric(self, fabric: Fabric):
        cursor = self._connection.cursor()
        values = fabric.get_values()
        cursor.execute(
            "INSERT INTO Fabrics (name, width, length, washed) VALUES (?,?,?,?)", values)
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM Fabrics')
        self._connection.commit()
