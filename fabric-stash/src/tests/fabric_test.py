import unittest
from entities.fabric import Fabric


class TestFabric(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_washed_fabric_sting_correct(self):
        fabric = Fabric("name", 100, 100, 1)
        self.assertEqual("name, 100cm x 100cm, washed: yes", str(fabric))

    def test_washed_to_string_correct_when_washed(self):
        fabric = Fabric("name", 100, 100, 1)
        self.assertEqual("yes", fabric.washed_to_str())

    def test_washed_to_string_correct_when_not_washed(self):
        fabric = Fabric("name", 100, 100, 0)
        self.assertEqual("no", fabric.washed_to_str())
