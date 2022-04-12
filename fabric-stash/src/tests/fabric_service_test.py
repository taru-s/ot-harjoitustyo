import unittest
from services.fabric_service import FabricService
from repositories import fabric_repository


class TestFabricService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = FabricService()
        self.service.delete_all()
        self.service.add_fabric("name", 100, 100, False)

    def test_added_fabric_returned(self):
        returned = self.service.get_all_fabrics()
        self.assertEqual("name, 100cm x 100cm, washed: no", returned[0])

    def test_get_fabric_by_name_returns_false_when_name_not_found(self):
        self.assertEqual(False, self.service.get_fabrics_by_name("testname"))

    def test_get_fabric_by_name_returns_fabric_when_name_found(self):
        returned = self.service.get_fabrics_by_name("name")
        self.assertEqual("name, 100cm x 100cm, washed: no", returned[0])
