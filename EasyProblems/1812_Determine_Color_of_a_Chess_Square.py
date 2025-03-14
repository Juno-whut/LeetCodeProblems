import unittest



class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        num = ord(coordinates[0]) % 2
        char = ord(coordinates[1]) % 2

        if num != char:
            return True
        return False

        



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().squareIsWhite

    def test1(self):
        self.assertFalse(self.s("a1"), False)

    def test2(self):
        self.assertTrue(self.s("h3"), True)


if __name__ == "__main__":
    unittest.main()