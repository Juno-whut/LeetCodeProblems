import unittest


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)
        stones = list(stones)
        jewels_stones = {}
        num_jewels = 0

        for jewel in jewels:
            jewels_stones[jewel] = 0
        
        for stone in stones:
            if stone in jewels_stones:
                jewels_stones[stone] += 1
        
        for k, v in jewels_stones.items():
            if v > 0:
                num_jewels += v
        return num_jewels




class TestJewelsInStones(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().numJewelsInStones("aA", "aAAbbbb"), 3)

    def test2(self):
        self.assertEqual(Solution().numJewelsInStones("z", "ZZ"), 0)
    

if __name__ == "__main__":
    unittest.main()