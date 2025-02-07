import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        maxlen = 0
        curr_length = set()
        for i in s:
            if i in curr_length:
                if len(curr_length) > maxlen:
                    maxlen = len(curr_length)
                curr_length.clear()
            curr_length.add(i)
        
        if len(curr_length) > maxlen:
            return len(curr_length)
        return maxlen
        


class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.s = Solution().lengthOfLongestSubstring

    def test1(self):
        self.assertEqual(self.s("ab cabcbb"), 4)

    def test2(self):
        self.assertEqual(self.s("bbbbb"), 1)

    def test3(self):
        self.assertEqual(self.s("pwwkew"), 3)

    def test4(self):
        self.assertEqual(self.s(""), 0)
    
    def test5(self):
        self.assertEqual(self.s("dvdf"), 3)


if __name__ == '__main__':
    unittest.main()