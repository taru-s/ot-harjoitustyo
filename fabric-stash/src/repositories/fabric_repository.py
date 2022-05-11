from entities.fabric import Fabric


class FabricRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all_fabrics(self) -> list:
        """Gets all fabrics from the database and returns them as a list of Fabric objects.

        Returns:
            list: List of Fabric objects.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics")
        rows = cursor.fetchall()

        return [Fabric(row["name"], row["width"], row["length"],
                       row["washed"]) for row in rows]

    def get_all_ids(self) -> list:
        """Gets all ids from the database and returns them as a list.

        Returns:
            list: List of integer ids.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT id FROM Fabrics")
        rows = cursor.fetchall()
        return [row["id"] for row in rows]

    def get_fabric_by_id(self, fabric_id) -> Fabric:
        """Gets the fabric with the given id from the database.

        Args:
            fabric_id (_type_): _description_

        Returns:
            Fabric: Returns the information of the matching id as a Fabric object.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics WHERE id = ?", [fabric_id])
        row = cursor.fetchone()

        if not row:
            return None

        return Fabric(row["name"], row["width"], row["length"],
                      row["washed"])

    def get_fabric_by_name(self, name_contains: str) -> list:
        """Gets fabrics by name from the database.

        Gets fabrics with a name containing the string provided as an argument.

        Args:
            name (str): String with which the fabrics will be searched for from the database

        Returns:
            list: List of Integer ids.
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics WHERE name LIKE ?",
                       ("%"+name_contains+"%",))
        rows = cursor.fetchall()

        return [row["id"] for row in rows]

    def get_fabrics_by_washed(self, washed: int) -> list:
        """Gets fabrics with the given washed status from the database.

        Args:
            washed (int): 0 for washed, 1 for not washed

        Returns:
            list: Returns a list of the ids of fabrics with the given washed status.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Fabrics WHERE washed = ?", [washed])
        rows = cursor.fetchall()

        return [row["id"] for row in rows]

    def add_fabric(self, fabric: Fabric):
        """Adds a fabric to the database.

        Takes a Fabric object as an argument, saves it's information to the database.
        Assigns a new unique integer id to the row in the database.

        Args:
            fabric (Fabric): A Fabric object with the information of the fabric to be added.
        """
        cursor = self._connection.cursor()
        values = fabric.get_values()
        cursor.execute(
            "INSERT INTO Fabrics (name, width, length, washed) VALUES (?,?,?,?)", values)
        self._connection.commit()

    def update_fabric_by_id(self, fabric_id: int, fabric: Fabric):
        """Updates the information of the fabric with the given information.

        Args:
            fabric_id (int): Id of the fabric to be updated
            fabric (Fabric): A Fabric object containing the new information of the fabric
                    to be updated.
        """
        cursor = self._connection.cursor()
        values = fabric.get_values()
        values.append(fabric_id)
        cursor.execute(
            "UPDATE Fabrics SET name=?, width=?, length=?, washed=? WHERE id = ?", values)
        self._connection.commit()

    def delete_all(self):
        """Deletes all information from the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM Fabrics')
        self._connection.commit()

    def delete_by_id(self, fabric_id: int):
        """Deletes the fabric by the given id from the database.

        Deletes the row with the if integer given as argument.

        Args:
            fabric_id (int): Integer id of the fabric to be deleted.
        """
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM Fabrics WHERE id = ?', [fabric_id])
        self._connection.commit()
