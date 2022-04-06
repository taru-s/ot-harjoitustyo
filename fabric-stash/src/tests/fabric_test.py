import unittest
from entities.fabric import Fabric


class TestFabricService(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_washed_fabric_sting_correct(self):
        fabric = Fabric("name", 100, 100, True)
        self.assertEqual("name, 100cm x 100cm, washed: yes", str(fabric))
