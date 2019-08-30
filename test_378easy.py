# Unittest for 378easy.py

import easy_378
import unittest

class Test_TestEasy378(unittest.TestCase):
    def test_warmup1(self):
        self.assertEqual(easy_378.warmup1([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]), ([5, 3, 2, 6, 2, 7, 2, 5]))
        self.assertEqual(easy_378.warmup1([4, 0, 0, 1, 3]), [4, 1, 3])
        self.assertEqual(easy_378.warmup1([1, 2, 3]), [1, 2, 3])
        self.assertEqual(easy_378.warmup1([0, 0, 0]), [])
        self.assertEqual(easy_378.warmup1([]), [])
    
    def test_warmup2(self):
        self.assertEqual(easy_378.warmup2([5, 1, 3, 4, 2]), [5, 4, 3, 2, 1])
        self.assertEqual(easy_378.warmup2([0, 0, 0, 4, 0]), [4, 0, 0, 0, 0])
        self.assertEqual(easy_378.warmup2([1]), [1])
        self.assertEqual(easy_378.warmup2([]), [])

if __name__ == '__main__':
    unittest.main()