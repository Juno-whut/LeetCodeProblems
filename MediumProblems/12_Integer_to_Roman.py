import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        Numerals = [
            (1000 , "M"),
            (900 , "CM"),
            (500 , "D"),
            (400 , "CD"),
            (100 , "C"),
            (90 , "XC"),
            (50 , "L"),
            (40 , "XL"),
            (10 , "X"),
            (9 , "IX"),
            (5 , "V"),
            (4 , "IV"),
            (1 , "I"),
        ]
        
        romanNumeral = ""

        for value, numeral in Numerals:
            if num == 0:
                break
            count = num // value
            num = num % value

            romanNumeral += numeral * count
        return romanNumeral
            


class TestIntToRoman(unittest.TestCase):
    def setUp(self):
        self.s = Solution().intToRoman
    
    def test1(self):
        self.assertEqual(self.s(3), "III")
    
    def test2(self):
        self.assertEqual(self.s(54), "LIV")
    
    def test3(self):
        self.assertEqual(self.s(1994), "MCMXCIV")




if __name__ == "__main__":
    unittest.main()