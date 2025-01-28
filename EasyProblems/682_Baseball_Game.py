import unittest


class Solution:
    def calPoints(self, operations) -> int:
        stack = []
        previous, previous2 = 0,0

        while operations:
            current_opp = operations.pop(0)

            if current_opp.isdigit():
                stack.append(int(current_opp))
                current_num = int(current_opp)
            
            if current_opp == '+':
                stack.append((previous + previous2))
                current_num = previous +previous2
            
            if current_opp == 'D':
                stack.append(previous*2)
                current_num = previous*2

            if current_opp == 'C':
                stack.pop()
                len_stack = len(stack)
                if len_stack > 0:
                    previous = stack[len_stack-1]
                    previous2 = stack[len_stack-2]
                else:
                    previous = 0
                    previous2 = 0
            else:
                previous2 = previous
                previous = current_num
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