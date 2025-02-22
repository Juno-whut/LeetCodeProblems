import unittest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        
        result = self.recursion(n, 1)
        return result
    
    def recursion(self, n, power):
        res = 2**power
        if res != n:
            self.recursion(n, power *2)
        elif res > n:
            return False
        return True



class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        return bin(n).count('1') == 1


class TestKthCharacter(unittest.TestCase):
    def setUp(self):
        self.s = Solution().isPowerOfTwo
    
    def test1(self):
        self.assertEqual(self.s(1), True)
    
    def test2(self):
        self.assertEqual(self.s(16), True)
    
    def test3(self):
        self.assertEqual(self.s(3), False)



if __name__ == '__main__':
    print(bin(-16))
    unittest.main()