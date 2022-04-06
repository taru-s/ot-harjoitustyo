
from entities.fabric import Fabric


class FabricRepository:
    def __init__(self) -> None:
        self._fabrics = {}

    def add_fabric(self, name, width=0, length=0, washed=False):
        self._fabrics[name] = Fabric(name, width, length, washed)

    def get_all_fabrics(self):
        return [str(f) for f in self._fabrics.values()]
