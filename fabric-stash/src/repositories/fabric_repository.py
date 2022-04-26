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

    def get_all_ids(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id FROM Fabrics")
        rows = cursor.fetchall()
        return [row["id"] for row in rows]

    def get_fabric_by_property(self, property_name, property_state):
        pass

    def get_fabric_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics WHERE name = ?", [name])
        rows = cursor.fetchall()

        return [Fabric(row["name"], row["width"], row["length"],
                       row["washed"]) for row in rows]

    def get_fabric_by_id(self, fabric_id):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics WHERE id = ?", [fabric_id])
        rows = cursor.fetchall()

        return [Fabric(row["name"], row["width"], row["length"],
                       row["washed"]) for row in rows]

    def get_fabric_by_washed(self, washed):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics WHERE washed = ?", [washed])
        rows = cursor.fetchall()

        return [Fabric(row["name"], row["width"], row["length"],
                       row["washed"]) for row in rows]

    def add_fabric(self, fabric: Fabric):
        cursor = self._connection.cursor()
        values = fabric.get_values()
        cursor.execute(
            "INSERT INTO Fabrics (name, width, length, washed) VALUES (?,?,?,?)", values)
        self._connection.commit()

    def update_fabric_by_id(self, fabric_id, fabric: Fabric):
        cursor = self._connection.cursor()
        values = fabric.get_values()
        values.append(fabric_id)
        cursor.execute(
            "UPDATE Fabrics SET name=?, width=?, length=?, washed=? WHERE id = ?", values)
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM Fabrics')
        self._connection.commit()

    def delete_by_id(self, fabric_id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM Fabrics WHERE id = ?', [fabric_id])
        self._connection.commit()
