from entities.fabric import Fabric

class FabricRepository:
    def __init__(self) -> None:
        self._fabrics = {}

    def add_fabric(self, fabric:Fabric):
        self._fabrics[fabric.name] = fabric

    def get_all_fabrics(self):
        return [str(f) for f in self._fabrics.values()]

    def get_fabric_by_name(self, name):
        if name in self._fabrics:
            return self._fabrics[name]
        return False
