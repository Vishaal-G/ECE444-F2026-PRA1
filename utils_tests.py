import unittest
from utils import utils


class TestUtils(unittest.TestCase):
    def test_reversed_int(self):
        self.assertEqual(utils.reversed(123), 321)
        self.assertEqual(utils.reversed(-450), -54)

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            utils.reversed("123")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            utils.reversed(12.3)

    def test_formatter_int(self):
        self.assertEqual(utils.formatter(8), {"binary": "1000", "octal": "10"})

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            utils.formatter("8")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils.formatter(8.5)


if __name__ == "__main__":
    unittest.main()