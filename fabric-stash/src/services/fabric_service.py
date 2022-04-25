from repositories.fabric_repository import FabricRepository
from entities.fabric import Fabric
from database_connection import get_database_connection


class FabricService:
    def __init__(self) -> None:
        self._repository = FabricRepository(get_database_connection())

    def add_fabric(self, name, width, length, washed):
        # if not name:
        #     return False
        # try:
        #     int(width)
        # except:
        #     return False
        # # if type(width) != int:
        # #     return False
        # if width < 1 or length < 1:
        #     return False

        fabric = Fabric(str(name), width, length, washed)
        self._repository.add_fabric(fabric)
        return True

    def edit_fabric(self, name):
        pass

    def get_all_fabrics(self):
        return self._repository.get_all_fabrics()

    def get_all_ids(self):
        return self._repository.get_all_ids()

    def get_fabrics_by_name(self, name):
        fabrics = self._repository.get_fabric_by_name(name)
        if not fabrics:
            return False
        return fabrics

    def get_fabric_by_id(self, fabric_id):
        fabrics = self._repository.get_fabric_by_id(fabric_id)
        if not fabrics:
            return False
        return fabrics

    def delete_fabric_by_id(self, fabric_id):
        self._repository.delete_by_id(fabric_id)

    def delete_all(self):
        self._repository.delete_all()
