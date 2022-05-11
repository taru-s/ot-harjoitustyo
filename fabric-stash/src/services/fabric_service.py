from typing import List
from repositories.fabric_repository import FabricRepository
from entities.fabric import Fabric
from database_connection import get_database_connection


class FabricService:
    """A class for handling fabric application logic.

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

    def get_fabrics_by_name(self, name_contains: str) -> List:
        """Get fabrics that contain the provided string in their name.

        Returns a list of the fabrics with a name containing the string given as an argument.
        If no fabrics with a name containing the string are found, returns None.

        Args:
            name (str): String to be compared to the database fabrics' names.

        Returns:
            List: List of ids of the found fabrics. None if no fabrics found by the name.
        """
        fabric_ids = self._repository.get_fabric_by_name(name_contains)
        if not fabric_ids:
            return None
        return fabric_ids

    def get_fabrics_by_washed(self, washed: int):
        """Gets fabrics with the given washed status.

        Args:
            washed (int): 0 for washed, 1 for not washed

        Returns:
            list: Returns a list of the ids of fabrics with the given washed status.
        """
        fabric_ids = self._repository.get_fabrics_by_washed(washed)
        if not fabric_ids:
            return None
        return fabric_ids

    def search_fabrics(self, name_contains: str, washed: int) -> list:
        """Searches for fabrics according to name and washed status.

        Name has to contain the string arg name_contains. Is empty, name can be anything.
        Washed status has to match the int arg washed.
        If washed = -1, washed status can be anything.

        Args:
            name_contains (str): name has to contain this string
            washed (int): washed status 1=washed, 0=not washed, -1=not included in search

        Returns:
            list: List of the fabric ids of fabrics matching the search criteria.
                    Returns None if no matches found.
        """
        name_contains = name_contains.strip()
        if washed == -1 and not name_contains:
            return self._repository.get_all_ids()
        if washed == -1:
            return self.get_fabrics_by_name(name_contains)
        if not name_contains:
            return self.get_fabrics_by_washed(washed)

        matching = []
        fabrics = self.get_fabrics_by_name(name_contains)
        if not fabrics:
            return None

        for i in fabrics:
            if self.get_fabric_by_id(i).washed == washed:
                matching.append(i)

        if not matching:
            return None
        return matching

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
