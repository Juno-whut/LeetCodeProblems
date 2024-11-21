import unittest


class Solution:
    def sumOfDigits(self, nums):
        min_num = min(nums)
        sum_digits = 0

        while min_num > 0:
            sum_digits += min_num % 10
            min_num = min_num // 10

        return int(sum_digits % 2 == 0)

        


class SumOfDigitsTest(unittest.TestCase):
    def test_basecase_1(self):
        nums = [1]
        self.assertEqual(Solution().sumOfDigits(nums), 0)
    
    def test_basecase_2(self):
        nums = [100]
        self.assertEqual(Solution().sumOfDigits(nums), 0)
    
    def test_numsincreasing(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(Solution().sumOfDigits(nums), 0)
    
    def test_decreasing(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2]
        self.assertEqual(Solution().sumOfDigits(nums), 1)
    
    def test_random(self):
        nums = [98, 45, 89, 56, 43, 12, 76, 34, 12]
        self.assertEqual(Solution().sumOfDigits(nums), 0)
    
    def test_all_samse(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(Solution().sumOfDigits(nums), 0)
    
    def test_million(self):
        nums = [1234567]
        self.assertEqual(Solution().sumOfDigits(nums), 1)


if __name__ == '__main__':
    print(9 % 1)
    print(9 % 10)
    print(93 % 10)
    print(930 % 10)
    print(930 // 10)
    print(93 // 10)
    print(33 % 2)
    print(22 % 2)
    unittest.main()