
from entities.fabric import Fabric


class FabricRepository:
    def __init__(self) -> None:
        self._fabrics = {}

    def add_fabric(self, name:str, width=0, length=0, washed=False):
        self._fabrics[str(name)] = Fabric(str(name), width, length, washed)

    def get_all_fabrics(self):
        return [str(f) for f in self._fabrics.values()]

    def get_fabric_by_name(self, name):
        if name in self._fabrics.keys():
            return self._fabrics[name]
        else:
            return False