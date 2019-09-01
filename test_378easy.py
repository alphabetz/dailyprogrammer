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

    def test_warmup3(self):
        self.assertEqual(easy_378.warmup3(7, [6, 5, 5, 3, 2, 2, 2]), False)
        self.assertEqual(easy_378.warmup3(5, [5, 5, 5, 5, 5]), False)
        self.assertEqual(easy_378.warmup3(5, [5, 5, 5, 5]), True)
        self.assertEqual(easy_378.warmup3(3, [1, 1]), True)
        self.assertEqual(easy_378.warmup3(1, []), True)
        self.assertEqual(easy_378.warmup3(0, []), False)
    
    def test_warmup4(self):
        self.assertEqual(easy_378.warmup4(4, [5, 4, 3, 2, 1]), [4, 3, 2, 1, 1])
        self.assertEqual(easy_378.warmup4(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]), [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2])
        self.assertEqual(easy_378.warmup4(1, [10, 10, 10]), [9, 10, 10])
        self.assertEqual(easy_378.warmup4(3, [10, 10, 10]), [9, 9, 9])
        self.assertEqual(easy_378.warmup4(1, [1]), [0])
    
    def test_hh(self):
        self.assertEqual(easy_378.hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]), False)
        self.assertEqual(easy_378.hh([4, 2, 0, 1, 5, 0]), False)
        self.assertEqual(easy_378.hh([3, 1, 2, 3, 1, 0]), True)
        self.assertEqual(easy_378.hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]), True)
        self.assertEqual(easy_378.hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]), True)
        self.assertEqual(easy_378.hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]), False)
        self.assertEqual(easy_378.hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]), False)
        self.assertEqual(easy_378.hh([2, 2, 0]), False)
        self.assertEqual(easy_378.hh([3, 2, 1]), False)
        self.assertEqual(easy_378.hh([1, 1]), True)
        self.assertEqual(easy_378.hh([1]), False)
        self.assertEqual(easy_378.hh([]), True)

if __name__ == '__main__':
    unittest.main()