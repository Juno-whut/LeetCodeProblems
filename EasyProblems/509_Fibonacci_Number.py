import unittest

class Solution:
    def __init__(self):
        self.fibDict = {
        }

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n ==2:
            return 1
        if n in self.fibDict:
            return self.fibDict[n]
        self.fibDict[n] = self.fib(n - 1) + self.fib(n - 2) 
        return self.fibDict[n]

    




class FibTest(unittest.TestCase):
    def test_1(self):
        n = 2
        self.assertEqual(Solution().fib(n), 1)
    def test2(self):
        n = 3
        self.assertEqual(Solution().fib(n), 2)
    def test3(self):
        n = 4
        self.assertEqual(Solution().fib(n), 3)
    def test4(self):
        n = 5
        self.assertEqual(Solution().fib(n), 5)
    def test5(self):
        n = 10
        self.assertEqual(Solution().fib(n), 55)


if __name__ == '__main__':
    unittest.main()