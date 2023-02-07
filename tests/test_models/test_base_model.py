""" Tests cases for the BaseModel class"""
import unittest
from models import base_model as bm

class BaseModelTest(unittest.TestCase):
    """ Tests the BaseModel class"""
    gloire = bm.BaseModel()

    def test_isDaughter(self):
        """Tests wether a given class is an instance ofthe BaseModel class"""
        print(self.gloire.__str__())
        self.assertIsInstance(self.gloire, bm.BaseModel, "Is not an instance of the BaseModel class")

        


if __name__ == "__main__":
    unittest.main()
