import unittest 



class Solution1:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        if len(trust) < n-1:
            return -1
        
        trust_scores = [0] * (n+1)

        for outgoing, incoming in trust:
            trust_scores[outgoing] -= 1
            trust_scores[incoming] += 1
        
        for i in range(1, n+1):
            if trust_scores[i] == n-1:
                return i
        return -1



"""
This is the second solution since when I submitted my first solution it was 50% in speed and 96% in space.
This solution frequently beats 90% or so in time and 25% in space. 

This solution uncomplicates my first solution by keep 2 arrays outdegrees and indegrees. indegrees holds
the amount of incoming connections and outdegrees holds the amount of outgoing connections if this were a graph.
indegrees are also initiated to an array the length of n+1 so the from numbers 0 - n+1. this makes its so that 
in the last for loop when we are looking for a num that has no outgoing connections but n-1 incoming connectins we
can return i becasue the ith position in the list is the ith number.
"""
class Solution2:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        if len(trust) < n-1:
            return -1
        
        indegrees = [0] * (n+1)
        outdegrees = [0] * (n+1)

        for a, b in trust:
            indegrees[b] += 1
            outdegrees[a] += 1
        
        for i in range(1, n+1):
            if indegrees[i] == n-1 and outdegrees[i] == 0:
                return i
        return -1



"""
This solution is the most obvious out of the 3. It uses a dictionary and keeps track each numbers trust value by 
incrementing the value of each number if it is currently in the dictionary and its value is not False. A numbers 
value is changed to False the first time it is seen as the first number in each pair this means that it trusts 
another number meaning it cant be the town judge after looping through the trust list to make the dictionary valid
we loop through the dictionary looking for a value that is equal to n-1 and then we return the key which is the 
correct number. The special cases this solution needs covered are when n equals 0 or when in which cases we return 
-1 or 1 accordingly
"""
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust) < n-1:
            return -1

        trustDict = {}
        for pair in trust:
            if pair[0] not in trustDict:
                trustDict[pair[0]] = 0
            trustDict[pair[0]] -= 1
            
            if pair[1] not in trustDict:
                trustDict[pair[1]] = 1
            else:
                trustDict[pair[1]] += 1
             
        
        for key, val in trustDict.items():
            if val == n-1:
                return key
        return -1


class TestFindJudge(unittest.TestCase):
    def setUp(self):
        self.s = Solution().findJudge
    
    def test1(self):
        self.assertEqual(self.s(2, [[1,2]]), 2)
    
    def test2(self):
        self.assertEqual(self.s(3, [[1,3], [2,3]]), 3)
    
    def test3(self):
        self.assertEqual(self.s(3, [[1,3], [2,3], [3,1]]), -1)
    
    def test4(self):
        self.assertEqual(self.s(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]), 3)
    
    def test5(self):
        self.assertEqual(self.s(2, [[1,2],[2,1]]), -1)


if __name__ == "__main__":
    unittest.main()