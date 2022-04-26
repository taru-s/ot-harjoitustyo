import unittest
from services.fabric_service import FabricService


class TestFabricService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = FabricService()
        self.service.delete_all()
        self.service.add_fabric("name", 100, 100, False)

    def test_added_fabric_returned(self):
        returned = self.service.get_all_fabrics()
        self.assertEqual("name, 100cm x 100cm, washed: no", str(returned[0]))

    def test_get_fabric_by_name_returns_false_when_name_not_found(self):
        self.assertEqual(False, self.service.get_fabrics_by_name("testname"))

    def test_get_fabric_by_name_returns_fabric_when_name_found(self):
        returned = self.service.get_fabrics_by_name("name")
        self.assertEqual("name, 100cm x 100cm, washed: no", str(returned[0]))

    def test_get_fabric_by_id_returns_fabric_when_id_found(self):
        returned = self.service.get_fabric_by_id(1)
        self.assertEqual("name, 100cm x 100cm, washed: no", str(returned))

    def test_delete_fabric_by_id_fabric_deleted(self):
        self.service.delete_fabric_by_id(1)
        returned = self.service.get_fabric_by_id(1)
        self.assertEqual(None, returned)

    def test_get_all_ids_returns_ids(self):
        self.service.add_fabric("name", 100, 100, False)
        self.service.add_fabric("name", 100, 100, False)
        
        returned = self.service.get_all_ids()
        self.assertEqual([1,2,3], returned)

    def test_edit_fabric_updates_fabric_info_correctly(self):
        self.service.edit_fabric(1, "new name", 2, 2, 1)
        returned = self.service.get_fabric_by_id(1)
        self.assertEqual("new name, 2cm x 2cm, washed: yes", str(returned))
