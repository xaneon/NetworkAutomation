import unittest
import Kap3_unittest_maths

class TestMaths(unittest.TestCase):
    """
    Usage:  python <test file name>.py -v
            for details.
    """
    def test_addition(self):
        result = Kap3_unittest_maths.addiere(3, 5)
        self.assertEqual(result, 8)

    def test_subtraktion(self):
        result = Kap3_unittest_maths.subtrahiere(5, 3)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()

