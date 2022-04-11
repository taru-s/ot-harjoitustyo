from repositories.fabric_repository import FabricRepository
from entities.fabric import Fabric
from database_connection import get_database_connection
from initialize_database import initialize_database


class FabricService:
    def __init__(self) -> None:
        self._repository = FabricRepository(get_database_connection())

    def add_fabric(self, name, width, length, washed):
        fabric = Fabric(name, width, length, washed)
        self._repository.add_fabric(fabric)

    def edit_fabric(self, name):
        pass

    def get_all_fabrics(self):
        return self._repository.get_all_fabrics()

    def get_fabric_by_name(self, name):
        return self._repository.get_fabric_by_name(name)
