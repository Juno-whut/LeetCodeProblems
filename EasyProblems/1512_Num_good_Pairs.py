import unittest


class Solution:
    def numIdenticalPairs(self, nums) -> int:
        repeats = {}
        good_pairs = 0
        for i in nums:
            if i in repeats:
                good_pairs += repeats[i]
                repeats[i] += 1
            else:
                repeats[i] = 1
        return good_pairs

    


class TestNumIdenticalPairs(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)
    
    def test2(self):
        self.assertEqual(Solution().numIdenticalPairs([1, 2, 3]), 0)
    
    def test3(self):
        self.assertEqual(Solution().numIdenticalPairs([1, 1, 1, 1]), 6)


if __name__ == "__main__":
    unittest.main()