import unittest


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        
        seen = {}
        for i in list(s):
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        for i in range(len(t)):
            if t[i] not in seen:
                return t[i]
           




class TestFindDifference(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findTheDifference("abcd", "abcde"), "e")
    
    def test2(self):
        self.assertEqual(Solution().findTheDifference("", "y"), "y")
    
    def test3(self):
        self.assertEqual(Solution().findTheDifference("a", "aa"), "a")


if __name__ == '__main__':
    unittest.main()