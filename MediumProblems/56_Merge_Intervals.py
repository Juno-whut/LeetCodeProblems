import unittest 



class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        curr = 0
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[curr][1]:
                curr += 1
                res.append(intervals[i])
            elif res[curr][1] <= intervals[i][1]:
                res[curr][1] = intervals[i][1] 
        return res



class TestMerge(unittest.TestCase):
    def setUp(self):
        self.s = Solution().merge
    
    def test_merge(self):
        self.assertEqual(self.s([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
    
    def test_merge1(self):
        self.assertEqual(self.s([[1,4],[4,5]]), [[1,5]])
    
    def test_merge2(self):
        self.assertEqual(self.s([[1,4], [0,4]]), [[0,4]])
    
    def test_merge3(self):
        self.assertEqual(self.s([[1,4], [0,1]]), [[0,4]])
    
    def test_merge4(self):
        self.assertEqual(self.s([[1,4], [0,0]]), [[0,0], [1,4]])
    
    def test_merge5(self):
        self.assertEqual(self.s([[1,4],[0,2],[3,5]]), [[0,5]])

    def test_merge6(self):
        self.assertEqual(self.s([[2,3],[4,5],[6,7],[8,9],[1,10]]), [[1,10]])

if __name__ == "__main__":
    unittest.main()