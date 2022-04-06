from repositories.fabric_repository import FabricRepository

class FabricService:
    def __init__(self) -> None:
        self._repository = FabricRepository()

    def add_fabric(self, name, width, length, washed):
        self._repository.add_fabric(name, width, length, washed)

    def edit_fabric(self, name):
        pass

    def get_all_fabrics(self):
        return self._repository.get_all_fabrics()

    def get_fabric_by_name(self, name):
        return self._repository.get_fabric_by_name(name)