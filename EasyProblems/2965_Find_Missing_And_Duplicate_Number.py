import unittest 


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        missing = None
        duplicate = None
        numbers = set(x for x in range(1, len(grid)**2+1))
        for i in grid:
            for j in i:
                if j in numbers:
                    numbers.remove(j)
                else:
                    duplicate = j
        missing = numbers.pop()
        return [duplicate, missing]


class TestFindMissingAndReapeatingValues(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findMissingAndRepeatedValues([[1,2,3], [3,4,5],[6,7,8]]), [9,3])
    

if __name__ == "__main__":
    unittest.main()