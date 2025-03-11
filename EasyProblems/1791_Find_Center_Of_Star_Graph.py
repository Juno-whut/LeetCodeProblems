import unittest


class Solution1:
    def findCenter(self, edges: list[list[int]]) -> int:
        length = len(edges)

        connections = [0] * (length+2)
        for a, b in edges:
            connections[a] += 1
            connections[b] +=1
        
        for i in range(1, length+2):
            if connections[i] == length:
                return i


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        visted = set()
        visted.add(edges[0][1])
        visted.add(edges[0][0])

        if edges[1][0] in visted:
            return edges[1][0]
        return edges[1][1]


class TestSolution(unittest.TestCase):
    def test_findCenter(self):
        self.assertEqual(Solution().findCenter([[1, 2], [2, 3], [4, 2]]), 2)
    
    def test1(self):
        self.assertEqual(Solution().findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]), 1)
    
    def test2(self):
        self.assertEqual(Solution().findCenter([[1,18],[18,2],[3,18],[18,4],[18,5],[6,18],[18,7],[18,8],[18,9],[18,10],[18,11],[12,18],[18,13],[18,14],[15,18],[16,18],[17,18]]), 18)


if __name__ == '__main__':
    unittest.main()