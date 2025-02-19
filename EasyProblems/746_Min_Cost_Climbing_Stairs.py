import unittest


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost1 = cost.copy()
        total_cost1 = self.helper(cost1, 0, 0, len(cost))
        cost.pop(0)
        total_cost2 = self.helper(cost, 1, 0, len(cost)-1)
        return min(total_cost1, total_cost2)

    def helper(self, cost: list[int], index: int, running_total: int, stairs: int) -> list[int]:
        
        if index == 0:
            minPrice = min(cost)
            running_total += minPrice
            stairs -= 2
        if index == 1:
            minPrice = min(cost)
            running_total += minPrice
            stairs -= 2

        cost.remove(minPrice)
        if stairs > 0:
            running_total = self.helper(cost, index, running_total, stairs)   
        return running_total
            

'''
Just learned that you cant use a price on a step behind you which is the reason for the current failures
so I will be changing this later so that it deciedes so that it is similiar to the normal climbing stairs solution but 
differs when adding new combinations. So that if a combinations total cost is greater than the lowest costing one we will 
not add it as a combination, and we will use a stack is the reverse of monotonic in senses that it is always necreasing and
then we will return the total cost on the top of the stack/end of the array
'''





class testMinCostClimbinStairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution().minCostClimbingStairs
    
    def test1(self):
        self.assertEqual(self.s([10, 15, 20]), 15)  
    
    def test2(self):
        self.assertEqual(self.s([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
        
    def test3(self):
        self.assertEqual(self.s([1,4,3,5,9,7]), 8)
        
    def test4(self): 
        self.assertEqual(self.s([1, 10, 7, 9, 15, 4]), 12)



if __name__ == "__main__":
    unittest.main()
