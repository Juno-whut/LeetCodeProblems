import unittest


class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        flowers_placed = 0
        empty_spots = 0
        flowerbed_len = len(flowerbed)
        flower_planted = False

        if n == 0:
            return True

        if flowerbed_len <= 2 and n == 0 or flowerbed_len == 1 and flowerbed[0] == 0:
            return True

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            flowers_placed += 1
        
        if flowerbed[flowerbed_len - 1] == 0 and flowerbed[flowerbed_len - 2] == 0:
            flowerbed[flowerbed_len - 1] = 1
            flowers_placed += 1
        
        if flowers_placed >= n:
            return True

        for i in range(1, flowerbed_len-1):
            if flower_planted and flowerbed[i] == 1:
                flowerbed[i-1] = 0
                flowers_placed -= 1
            flower_planted = False

            if flowers_placed >= n:
                return True

            if flowerbed[i] == 0:
                empty_spots += 1
            else:
                empty_spots = 0
            
            if empty_spots == 2:
                flowerbed[i] = 1
                empty_spots = 0
                flowers_placed += 1
                flower_planted = True
        return False




class TestCanPlaceFlowers(unittest.TestCase):
    def test_can_place_flowers(self):
        self.assertTrue(Solution().canPlaceFlowers([1,0,0,0,1], 1), True)
    
    def test_can_place_flowers_2(self):
        self.assertFalse(Solution().canPlaceFlowers([1,0,0,0,1], 2), False)
    
    def test_can_place_flowers_3(self):
        self.assertTrue(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2), True)
    
    def test_can_place_flowers_4(self):
        self.assertFalse(Solution().canPlaceFlowers([1,0,1,0,0,1,0], 1), False)

    def test_can_place_flowers_5(self):
        self.assertTrue(Solution().canPlaceFlowers([1,0,0,0,1,0,0], 2), True)
    
    def test_can_place_flowers_6(self):
        self.assertTrue(Solution().canPlaceFlowers([0,0], 1), True)


if __name__ == "__main__":
    unittest.main()