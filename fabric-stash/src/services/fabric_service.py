from typing import List
from repositories.fabric_repository import FabricRepository
from entities.fabric import Fabric
from database_connection import get_database_connection


class FabricService:
    """A class for wrapping and handling fabric database.

    """
    def __init__(self) -> None:
        self._repository = FabricRepository(get_database_connection())

    def add_fabric(self, name: str, width: int, length: int, washed: int):
        """Add a new fabric to the database.

        Args:
            name (str): Name of the fabric.
            width (int): Width of fabric in centimeters.
            length (int): Length of fabric in centimeters.
            washed (int): Has the fabric been washed? Can be 0 for false or 1 for true.
        """

        fabric = Fabric(str(name), width, length, washed)
        self._repository.add_fabric(fabric)

    def edit_fabric(self, fabric_id: int, name: str, width: int, length: int, washed: int):
        """Edits fabric with the given id to have the properties provided.

        Args:
            fabric_id (int): Id of the fabric in the database.
            name (str): Name of the fabric.
            width (int): Width of fabric in centimeters.
            length (int): Length of fabric in centimeters.
            washed (int): Has the fabric been washed? Can be 0 for false or 1 for true.
        """

        fabric_info = Fabric(str(name), width, length, washed)
        self._repository.update_fabric_by_id(fabric_id, fabric_info)

    def get_all_fabrics(self) -> list:
        """Gets all fabrics as Fabric objects from the database.

        Returns:
            list: List of Fabric objects.
        """
        return self._repository.get_all_fabrics()

    def get_all_ids(self) -> list:
        """Gets all fabric ids from the database.

        Returns:
            list: List of fabric ids (int).
        """
        return self._repository.get_all_ids()

    def get_fabrics_by_name(self, name: str) -> List:
        """Get fabrics that have the provided name.

        Returns a list of the fabrics with a name matching the name given as an argument.
        If no fabrics with the name are found, returns None.

        Args:
            name (str): String to be compared to the database fabrics' names.

        Returns:
            List: List of ids of the found fabrics. None if no fabrics found by the name.
        """
        fabric_ids = self._repository.get_fabric_by_name(name)
        if not fabric_ids:
            return None
        return fabric_ids

    def get_fabric_by_id(self, fabric_id: int) -> Fabric:
        """Returns the Fabric matching the given id from the database.

        Returns the fabric as a Fabric object. If no fabric with the given id is found,
        returns None.

        Args:
            fabric_id (int): Id to be searached for from the database.

        Returns:
            Fabric: Returns the fabric with id matching the argument as a Fabric object.
                If no fabric with the id is found, returns None.
        """
        fabric = self._repository.get_fabric_by_id(fabric_id)
        if not fabric:
            return None
        return fabric

    def delete_fabric_by_id(self, fabric_id: int):
        """Deletes a fabric by the given id.

        Args:
            fabric_id (int): Id of the fabric to be deleted.
        """
        self._repository.delete_by_id(fabric_id)

    def delete_all(self):
        """Deletes all fabrics from the database.
        """
        self._repository.delete_all()
