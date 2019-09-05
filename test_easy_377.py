import easy_377
import unittest

class Test_TestEasy377(unittest.TestCase):
    
    def test_easy_377(self):
        self.assertEqual(easy_377.robot(25, 18, 6, 5), 12)
        self.assertEqual(easy_377.robot(10, 10, 1, 1), 100)
        self.assertEqual(easy_377.robot(12, 34, 5, 6), 10)
        self.assertEqual(easy_377.robot(12345, 678910, 1112, 1314), 5676)
        self.assertEqual(easy_377.robot(5, 100, 6, 1), 0)

if __name__ == '__main__':
    unittest.main()