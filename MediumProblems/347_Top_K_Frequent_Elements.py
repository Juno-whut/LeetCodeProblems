import unittest 


class Solution:
    def topKFrequent(self, nums, k: int):
        if len(nums) == k:
            return nums

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        max_freq = max(freq.values())

        buckets = [[] for i in range(max_freq+1)]

        for key, value in freq.items():
            buckets[value].append(key)
        
        result = []
        for freq in range(max_freq, 0, -1):
            result.extend(buckets[freq])
            if k - len(result) == 0:
                return result

        

class TopKFrequentTest(unittest.TestCase):
    def test_basecase_1(self):
        self.assertEqual(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
    
    def test_basecase_2(self):
        self.assertEqual(Solution().topKFrequent([1], 1), [1])
    
    def test_basecase_3(self):
        self.assertEqual(Solution().topKFrequent([1, 2], 2), [1, 2])
    
    def test_basecase_4(self):
        self.assertEqual(Solution().topKFrequent([3, 0, 1, 0], 1), [0])


if __name__ == "__main__": 
    unittest.main()
