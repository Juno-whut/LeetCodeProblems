import unittest


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            m = (left + right) // 2
            current = m * (m + 1) // 2
            if current == n:
                return m
            if current < n:
                left = m + 1
            else:
                right = m - 1
        return right
        

class TestAreangeCoins(unittest.TestCase):
    def setUp(self):
        self.s = Solution().arrangeCoins

    def test1(self):
        self.assertEqual(self.s(5), 2)

    def test2(self):
        self.assertEqual(self.s(8), 3)
    
    def test3(self):
        self.assertEqual(self.s(1), 1)

    def test4(self):
        self.assertEqual(self.s(24), 6)


if __name__ == '__main__':
    unittest.main()