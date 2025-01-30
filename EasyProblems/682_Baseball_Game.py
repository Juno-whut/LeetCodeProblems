import unittest


class Solution:
    def calPoints(self, operations) -> int:
        stack = []

        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(2 * stack[-1])
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
            
        return sum(stack)


class TestCalcPoints(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)
    
    def test2(self):
        self.assertEqual(Solution().calPoints(["1", "C"]), 0)
    
    def test3(self):
        self.assertEqual(Solution().calPoints(["5", "5", "5", "5", "5"]), 25)


if __name__ == "__main__":
    unittest.main()