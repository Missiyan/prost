import unittest

def pechat():
    print("это моя лаба")

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = pechat()
        self.assertEqual(result, "это моя лаба")

if __name__ == '__main__':
    unittest.main()