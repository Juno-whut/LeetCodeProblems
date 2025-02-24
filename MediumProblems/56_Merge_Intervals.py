import unittest 



class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        arrlen = len(intervals)

        if arrlen == 1:
            return intervals
        
        left = 0
        right = 1
        while left < right < arrlen:
            if intervals[left] == [0,0] or intervals[right] == [0,0]:
                    intervals.insert(0, [0,0])
                    intervals.pop(left+1) if intervals[left+1] == [0,0] else intervals.pop(right+1)
                    left += 1 
                    right += 1
                    arrlen -= 1
            elif intervals[left][1] == intervals[right][1]:
                intervals.pop(left)
                arrlen -= 1
                left += 1
                right += 1
            elif intervals[left][1] >= intervals[right][0]:
                maxleft = max(intervals[left])
                minleft = min(intervals[left])
                maxright = max(intervals[right])
                minright = min(intervals[right])

                intervals.pop(right)
                intervals[left] = [min(minleft, minright), max(maxleft, maxright)]
                arrlen -= 1
            elif intervals[right][0] < intervals[left][0]:
                intervals.pop(left)
                arrlen -= 1
                left -= 1
                right -= 1
            else:
                left += 1
                right += 1
        return intervals



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