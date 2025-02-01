import unittest


class IsBalancedTest(unittest.TestCase):

    def test_failed_1(self):
        s = '10'
        self.assertEqual(Solution().isBalanced(s), False)
    def test_basecase_1(self):
        s = "9218" # True
        self.assertEqual(Solution().isBalanced(s), True)

    def test_basecase_2(self):
        s = "921" # False
        self.assertEqual(Solution().isBalanced(s), False)
    
    def test_basecase_3(self):
        s = "101010101010101010101010101010101010101010101010110101010101010010101010011010101010101010101010101010" # False
        self.assertEqual(Solution().isBalanced(s), False)
    
    def test_case4(self):
        s = "0000000000000000000000000000000000000000000000000000" # True
        self.assertEqual(Solution().isBalanced(s), True)
    
    def test_case5(self):
        s = '1111111111' # True
        self.assertEqual(Solution().isBalanced(s), True)




class Solution:
    def isBalanced(self, num):
        num_arr = list(num)
        odd = 0
        even = 0
        for i in range(len(num_arr)):
            if i == 0:
                odd += int(num_arr[i])
            elif i % 2 == 0:
                odd += int(num_arr[i])
            else:
                even += int(num_arr[i])

        if odd == 0 and even == 0:
            return True
        
        result = odd - even 
        if result == 0:
            return True
        return False


if __name__ == '__main__':
    unittest.main()