import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        relist = []
        while max(l1,l2):
            num1 = 0
            num2 = 0
            if l1:
                num1 = l1.pop()

            if l2:  
                num2 = l2.pop()

            total = num1 + num2 + carry
            carry = total // 10
            total = total % 10
            relist.append(total)
            
        if carry:
            relist.append(carry)
        return relist



class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.s = Solution().addTwoNumbers
    
    def test1(self):
        self.assertEqual(Solution().addTwoNumbers([2,4,3], [5,6,4]), [7,0,8])
    
    def test2(self):
        self.assertEqual(Solution().addTwoNumbers([0], [0]), [0])
    
    def test3(self):
        self.assertEqual(Solution().addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]), [8,9,9,9,0,0,0,1])


if __name__ == '__main__':
    unittest.main()