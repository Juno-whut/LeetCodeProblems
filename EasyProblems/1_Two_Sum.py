import unittest

"""
So I did this problem before I started this repository. 
When I didnt take the time to think about the problem, time and space complexity, or documenting it.
So that being said the solution I currently have is the brute force option so it is O(n^2) time and O(1) space.
That being said, after thinking about it for a bit I realized that I could make it more efficient 
(due to the end of the problem description challenging me to do it in linear time)
"""

class Solution:
    def twoSum(self, nums, target: int):
        hashtable = {}
        for num in range(len(nums)):
            possible_match = target - nums[num]
            if possible_match in hashtable:
                return [num, hashtable[possible_match]]
            hashtable[nums[num]] = num

        return [] 

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().twoSum([2,7,11,15], 9), [1,0])
    
    def test2(self):
        self.assertEqual(Solution().twoSum([3,2,4], 6), [2,1])
    
    def test3(self):
        self.assertEqual(Solution().twoSum([3,2,4], 10), [])


if __name__ == '__main__':
    unittest.main()