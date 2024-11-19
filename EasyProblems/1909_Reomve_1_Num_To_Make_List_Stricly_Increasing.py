import unittest


class Solution:
    def canBeIncreasing(self, nums):
        if len(nums) == 2:
            return True
        
        count = 0
        num_before_removed = 0
        num_removed = False
        if nums[0] >= nums[1]:
            count += 1
        
        for i in range(1, len(nums)-1):
            if num_removed:
                if num_before_removed == i-1:
                    if nums[i-1] >= nums[i+1]:
                        return False
                    
                if num_before_removed == i-2:
                    if nums[i-2] >= nums[i+1]:
                        return False
                num_before_removed = 0
                num_removed = False

            if nums[i] >= nums[i+1]:
                if i+2 <= len(nums)-1:
                    if nums[i] >= nums[i+2]:
                        if nums[i-1] < nums[i+1] < nums[i+2]:
                            count += 1
                        else:
                            return False
                    if nums[i+1] >= nums[i+2]:
                        num_before_removed = i+1
                        num_removed = True
                        count += 1
                    if nums[i] < nums[i+2] and nums[i+1] < nums[i+2]:
                        num_removed = True
                        count += 1
                else:
                    count += 1

            if count > 1:
                    return False 
        return True

 
class StrictlyIncreasingTest(unittest.TestCase):
    
    def test_basecase_1(self):
        # Arrange
        nums = [1, 1]
        # Act & Assert
        self.assertTrue(Solution().canBeIncreasing(nums))

    def test_basecase_2(self):
        # Arrange
        nums = [100, 21, 102]
        # Act & Assert
        self.assertTrue(Solution().canBeIncreasing(nums))
    
    def test_all_increasing(self):
        # Arrange
        nums= [1, 2, 3]
        # Act & Assert
        self.assertTrue(Solution().canBeIncreasing(nums))
    
    def test_all_same(self):
        # Arrange
        nums = [1, 1, 1]
        # Act & Assert
        self.assertFalse(Solution().canBeIncreasing(nums))
    
    def test_1_removed(self):
        # Arrange
        nums = [1,2,10,5,7]
        # Act & Assert
        self.assertTrue(Solution().canBeIncreasing(nums))
    
    def test_2_sepate_removed(self):
        # Arrange
        nums = [2,10,5,9,7] 
        # Act & Assert
        self.assertFalse(Solution().canBeIncreasing(nums))
    
    def test_double_remove(self):
        # Arrange
        nums = [2,3,1,2]
        # Act & Assert
        self.assertFalse(Solution().canBeIncreasing(nums))
    
    def test_2_increasing_dreasing_increasing(self):
        # Arrange
        nums = [5, 7, 1, 6]
        # Act & Assert
        self.assertFalse(Solution().canBeIncreasing(nums))


if __name__ == "__main__":
    unittest.main()
