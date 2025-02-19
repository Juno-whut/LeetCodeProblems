import unittest


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        if number[0] == digit and (number[-1] == digit):
            return number[1:] if int(number[1]) >= int(digit) else number[:digit]
        lennumber = len(number)-1
        index = lennumber
        while index >= 0:
            if digit == number[index]:
                return number[:index] + number[index+1:] if index != lennumber else number[:index]
            index -= 1



class TestRemoveDigit(unittest.TestCase):
    def setUp(self):
        self.s = Solution().removeDigit
    
    def test1(self):
        self.assertEqual(self.s("123", 3), "12")
    
    def test2(self):
        self.assertEqual(self.s("1231", "1"), "231")
    
    def test3(self):
        self.assertEqual(self.s("551", "5"), "51")
    
    def test4(self):
        self.assertEqual(self.s("58577", "5"), "5877")


if __name__ == '__main__':
    unittest.main()