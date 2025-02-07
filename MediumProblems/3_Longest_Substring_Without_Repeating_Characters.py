import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        start, end = 0, 0
        longest = 0

        for i in range(len(s)):
            if s[i] in hashmap:
                if longest < (end - start):
                    longest = end - start
                if start < (hashmap[s[i]] + 1):   
                    start = hashmap[s[i]] + 1
                hashmap[s[i]] = i
            else:
                hashmap[s[i]] = i
            end += 1
        
        if longest < (end - start):
            return end - start
        return longest
        


class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.s = Solution().lengthOfLongestSubstring

    def test1(self):
        self.assertEqual(self.s("ab cabcbb"), 4)

    def test2(self):
        self.assertEqual(self.s("bbbbb"), 1)

    def test3(self):
        self.assertEqual(self.s("abba"), 2)

    def test4(self):
        self.assertEqual(self.s(""), 0)
    
    def test5(self):
        self.assertEqual(self.s("dvdf"), 3)


if __name__ == '__main__':
    unittest.main()