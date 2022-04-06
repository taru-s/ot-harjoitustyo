import unittest
from services.fabric_service import FabricService


class TestFabricService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = FabricService()

    def test_added_fabric_returned(self):
        self.service.add_fabric("name", 100, 100, False)
        returned = self.service.get_fabrics()
        self.assertEqual("name, 100cm x 100cm, washed: no", returned[0])
