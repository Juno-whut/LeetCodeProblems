import unittest


class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        pascalsTriangle = self.generate(numRows - 1)
        newRow = [1] * numRows

        for i in range(1, numRows -1):
            newRow[i] = pascalsTriangle[-1][i-1] + pascalsTriangle[-1][i]
        
        pascalsTriangle.append(newRow)
        return pascalsTriangle


class TestPascalsTriangle(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
    
    def test2(self):
        self.assertEqual(Solution().generate(1), [[1]])
    
    def test3(self):
        self.assertEqual(Solution().generate(0), [])
    
    def test4(self):
        self.assertEqual(Solution().generate(2), [[1], [1, 1]])


if __name__ == '__main__':
    unittest.main()