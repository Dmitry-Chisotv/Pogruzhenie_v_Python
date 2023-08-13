
import unittest
from task1 import Circle

class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Circle(1)
        self.r2 = Circle(10)
        self.r3 = Circle(3)


    def test_created(self):
        self.assertEqual(self.r1, Circle(1))


    def test_perimetr(self):
        self.assertEqual(self.r2.calc_perimetr(), 62.83185307179586)


    def test_area(self):
        self.assertEqual(self.r3.calc_area(), 28.274333882308138)


if __name__ == '__main__':
    unittest.main(verbosity=2)