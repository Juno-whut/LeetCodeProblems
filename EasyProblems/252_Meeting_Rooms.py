import unittest



class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


class TestCanAttendMeetings(unittest.TestCase):
    def test1(self):
        self.assertFalse(Solution().canAttendMeetings([[0,30],[5,10],[15,20]]), False)
    
    def test2(self):
        self.assertTrue(Solution().canAttendMeetings([[7,10],[2,4]]), True)


if __name__ == '__main__':
    unittest.main()