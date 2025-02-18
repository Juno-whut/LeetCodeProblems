import unittest




class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
        lenS = len(s)-1
        currentLetter = None
        previousLetter = s[0]
        total = 0
        i = 1
        while i <= lenS:

            currentLetter = s[i]
            if (previousLetter == "I" or previousLetter == "X" or previousLetter == "C") and (previousLetter != currentLetter):
                total += values[(previousLetter + currentLetter)]
                if i + 1 <= lenS:
                    previousLetter = s[i + 1]
                    i += 1
            else:
                total += values[previousLetter]
                previousLetter = currentLetter
            i += 1
        return total if previousLetter+currentLetter in values.items() else total + values[currentLetter]
        







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