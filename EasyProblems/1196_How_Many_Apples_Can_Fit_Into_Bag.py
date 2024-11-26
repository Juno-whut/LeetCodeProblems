import unittest


class Solution:
    def maxNumberOfApples(self, weight) -> int:
        total_weight = 0
        count = 0
        
        for i in sorted(weight):
            if (i + total_weight) <= 5000:
                count += 1
                total_weight += i
        return count




class MaxNumberOfApplesTest(unittest.TestCase):
    def test_basecase_1(self):
        weight = [100, 200, 150, 1000]
        self.assertEqual(Solution().maxNumberOfApples(weight), 4)
    
    def test_basecase_2(self):
        weight = [1000, 1000, 1000, 1000, 1000, 1000]
        self.assertEqual(Solution().maxNumberOfApples(weight), 5)
    
    def test_basecase_3(self):
        weight = [1, 2, 3, 5, 10]
        self.assertEqual(Solution().maxNumberOfApples(weight), 5)
    

if __name__ == "__main__":
    unittest.main()