import unittest



class Solution:
    def minMaxDifference(self, num: int) -> int:
        Max_Num = list(str(num))
        Min_Num = list(str(num))
        if len(Max_Num) == 1:
            return 9
        
        digit_picked = None
        for i in range(len(Max_Num)):
            if digit_picked:
                if Max_Num[i] == digit_picked:
                    Max_Num[i] = '9'
            elif Max_Num[i] < '9':
                digit_picked = Max_Num[i]
                Max_Num[i] = '9'
        Max_Num = int("".join(Max_Num))
        
        digit_picked = None
        for i in range(len(Min_Num)):
            if digit_picked:
                if Min_Num[i] == digit_picked:
                    Min_Num[i] = '0'
            elif Min_Num[i] != '0':
                digit_picked = Min_Num[i]
                Min_Num[i] = '0'
        Min_Num = int("".join(Min_Num))
        return Max_Num - Min_Num
    





class MinMaxDiffTest(unittest.TestCase):
    def test_leet_1(self):
        # Arrange
        num = 11891
        # Act & Assert
        self.assertEqual(Solution().minMaxDifference(num), 99009)
    
    def test_leet_2(self):
        num = 90
        self.assertEqual(Solution().minMaxDifference(num), 99)
    
    def test_basecase_1(self):
        num = 1
        self.assertEqual(Solution().minMaxDifference(num), 9) # if num is single digit the output is 9


if __name__ == "__main__":
    unittest.main()