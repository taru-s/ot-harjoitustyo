import unittest
from services.fabric_service import FabricService


class TestFabricService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = FabricService()
        self.service.add_fabric("name", 100, 100, False)

    def test_added_fabric_returned(self):
        returned = self.service.get_all_fabrics()
        self.assertEqual("name, 100cm x 100cm, washed: no", returned[0])

    def test_get_fabric_by_name_returns_false_when_name_not_found(self):
        self.assertEqual(False, self.service.get_fabric_by_name("testname"))

    def test_get_fabric_by_name_returns_fabric_when_name_found(self):
        returned = str(self.service.get_fabric_by_name("name"))
        self.assertEqual("name, 100cm x 100cm, washed: no", returned)
