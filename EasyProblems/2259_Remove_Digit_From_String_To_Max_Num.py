import unittest


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        total = "0"
        for i in range(len(number)):
            if number[i] == digit:
                temp = number[:i] + number[i+1:]
                if temp > total:
                    total = temp
        return total
        




class TestRemoveDigit(unittest.TestCase):
    def setUp(self):
        self.s = Solution().removeDigit
    
    def test1(self):
        self.assertEqual(self.s("123", "3"), "12")
    
    def test2(self):
        self.assertEqual(self.s("1231", "1"), "231")
    
    def test3(self):
        self.assertEqual(self.s("551", "5"), "51")
    
    def test4(self):
        self.assertEqual(self.s("58577", "5"), "8577")
    
    def test5(self):
        self.assertEqual(self.s("23", "2"), "3")


if __name__ == '__main__':
    unittest.main()