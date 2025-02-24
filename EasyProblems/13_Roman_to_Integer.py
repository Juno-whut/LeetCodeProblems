import unittest




class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50,"C": 100, "D": 500, "M": 1000}
        
        total = values[s[-1]]
        for i in reversed(range(len(s)-1)):
            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
        
        







class testRomanToInt(unittest.TestCase):
    def setUp(self):
        self.s = Solution().romanToInt
    
    def test1(self):
        self.assertEqual(self.s("III"), 3)
    
    def test2(self):
        self.assertEqual(self.s("LVIII"), 58)
    
    def test3(self):
        self.assertEqual(self.s("MCMXCIV"), 1994)
    
    def test4(self):
        self.assertEqual(self.s("M"), 1000)

    def test5(self):
        self.assertEqual(self.s("CM"), 900)

    def test6(self):
        self.assertEqual(self.s("XC"), 90)

    def test7(self):
        self.assertEqual(self.s("IX"), 9)

    def test8(self):
        self.assertEqual(self.s("IV"), 4)

    def test9(self):
        self.assertEqual(self.s("V"), 5)




if __name__ == '__main__':
    unittest.main()