import unittest
from collections import deque

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


class TestMinStack(unittest.TestCase):

    def test_1(self):
        minStack = MinStack()
        minStack.push(2)
        minStack.push(0)
        minStack.push(3)
        minStack.push(0)
        self.assertEqual(minStack.getMin(), 0)
        minStack.pop()
        self.assertEqual(minStack.getMin(), 0)
        minStack.pop()
        self.assertEqual(minStack.getMin(), 0)
        minStack.pop()
        self.assertEqual(minStack.getMin(), 2)
    
    def test_2(self):
        minStack = MinStack()
        minStack.push(646)
        minStack.push(2147646)
        minStack.push(2147483647)
        self.assertEqual(minStack.getMin(), 646)
    
    def test_3(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        minStack.getMin()
        minStack.pop()
        minStack.top()
        self.assertEqual(minStack.getMin(), -2)


if __name__ == '__main__':
    unittest.main()