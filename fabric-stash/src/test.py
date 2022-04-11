
from repositories.fabric_repository import FabricRepository
from initialize_database import get_database_connection
from entities.fabric import Fabric

fabric_repository = FabricRepository(get_database_connection())
fabric_repository.add_fabric(Fabric("testi", 100, 200, 0))
print(fabric_repository.get_all_fabrics())