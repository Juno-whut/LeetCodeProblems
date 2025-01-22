import unittest


class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)
        moves = 0
        for i in range(len(sorted_seats)-1, -1, -1):
            student = sorted_students.pop()
            moves += abs(sorted_seats[i]-student)
        return moves
            


class TestMinMovesToSeat(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().minMovesToSeat([3, 1, 5], [2, 7, 4]), 4)
    
    def test2(self):
        self.assertEqual(Solution().minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]), 7)


if __name__ == '__main__':
    unittest.main()