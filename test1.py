import unittest

def pechat(a,b):
    return a - b

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = pechat(3,8)
        self.assertEqual(result, -5)

if __name__ == '__main__':
    unittest.main()