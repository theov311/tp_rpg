# tests/test_basic.py
import unittest

class BasicTest(unittest.TestCase):
    def test_example(self):
        self.assertTrue(False)  # Ce test échouera

if __name__ == '__main__':
    unittest.main()

