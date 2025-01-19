import unittest


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0



class NimTest(unittest.TestCase):
    def test_1(self):
        n = 4
        self.assertEqual(Solution().canWinNim(n), False)
    
    def test_2(self):
        n = 3
        self.assertEqual(Solution().canWinNim(n), True)
    
    def test_3(self):
        n = 12
        self.assertEqual(Solution().canWinNim(n), False)
    


if __name__ == '__main__':
    unittest.main()