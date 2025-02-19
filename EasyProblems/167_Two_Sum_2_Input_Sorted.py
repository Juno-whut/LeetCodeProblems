import unittest


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution().twoSum
    
    def test1(self):
        self.assertEqual(self.s([2,3,4], 6), [1,3])

    def test2(self):
        self.assertEqual(self.s([5,25,75], 100), [2,3])

    def test3(self):
        self.assertEqual(self.s([2,7,11,15], 9), [1,2])

    def test4(self):
        self.assertEqual(self.s([-1,0], -1), [1,2])


if __name__ == '__main__':
    unittest.main()