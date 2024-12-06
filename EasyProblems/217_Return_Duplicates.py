import unittest

class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = set()
        for i in nums():
            if i in seen:
                return True
            seen.add(i)
        return False
        

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().containsDuplicate([1,2,3,4,1,2]), True)
    
    def test2(self):
        self.assertEqual(Solution().containsDuplicate(1,2,3,4,5,6,7,8,9), False)