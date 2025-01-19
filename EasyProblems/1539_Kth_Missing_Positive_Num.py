import unittest

class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        left, right = 0, len(arr) -1
        
        while left <= right:
            pivot = (left + right) // 2
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return left + k



class TestfindKthPositive(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findKthPositive([2, 3, 4, 7, 11], 5), 9)
    
    def test3(self):
        self.assertEqual(Solution().findKthPositive([1, 2, 3, 4], 2), 6)   

    def test2(self):
        self.assertEqual(Solution().findKthPositive([2], 1), 1) 


if __name__ == '__main__':
    unittest.main()


"""

This was my first solution to this problem which is not wrong but not optimal
-----------------------------------------------------------------------------
class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        missing_nums, expected_num, arr_num = 0, 0, None

        while missing_nums < k:
            expected_num += 1

            if not arr_num and arr:
                arr_num = arr.pop(0)
            
            if expected_num == arr_num:
                arr_num = None
            else:
                missing_nums += 1

        return expected_num 
"""