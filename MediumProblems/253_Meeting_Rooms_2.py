import unittest


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0
        
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)

        num_meetings = len(intervals)
        start, end, rooms = 0, 0, 0

        while start < num_meetings:
            if start_times[start] >= end_times[end]:
                rooms -= 1
                end += 1
            
            rooms += 1
            start += 1
        return rooms

class TestMinMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.s = Solution().minMeetingRooms 
    
    def test1(self):
        self.assertEqual(self.s([[0,30],[5,10],[15,20]]),2)
    
    def test2(self):
        self.assertEqual(self.s([[7,10],[2,4]]), 1)


if __name__ == '__main__':
    unittest.main()