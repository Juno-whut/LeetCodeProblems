import unittest

class Solution:
    def distributeCandies(self, candyType) -> int:
        return min((len(candyType)//2),(len(set(candyType))))
        candy_to_eat = len(candyType) // 2 
        candy_types = len(set(candyType))
        if candy_types > candy_to_eat:
            return candy_to_eat
        return candy_types





class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().distributeCandies([1,1,2,2,3,3]), 3)
    
    def test2(self):
        self.assertEqual(Solution().distributeCandies([1,1,2,3]), 2)
    
    def test3(self):
        self.assertEqual(Solution().distributeCandies([6,6,6,6]), 1)
    


if __name__ == "__main__":
    unittest.main()