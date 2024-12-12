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

        for i in list(t):
            if i in seen and (seen[i] == 0):
                return i
            elif i not in seen:
                return i
            elif i in seen:
                seen[i] -= 1
           




class TestFindDifference(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findTheDifference("abcd", "abcde"), "e")
    
    def test2(self):
        self.assertEqual(Solution().findTheDifference("", "y"), "y")
    
    def test3(self):
        self.assertEqual(Solution().findTheDifference("a", "aa"), "a")


if __name__ == '__main__':
    unittest.main()