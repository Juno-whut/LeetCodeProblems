import unittest


class Solution:
    def decrypt(self, code, k: int):
        lencode = len(code)
        decrypted_arr = [0] * lencode
        # base case 1
        if k == 0:
            return decrypted_arr
        
        start, end, window_sum = 1, k, 0
        #set up window
        if k < 0:
            start = lencode- abs(k)
            end = lencode -1
            
        for i in range(start, end+1):
            window_sum += code[i]

        for i in range(lencode):
            decrypted_arr[i] = window_sum
            window_sum -= code[start % lencode]
            window_sum += code[(end+1) % lencode]
            start += 1
            end += 1
        return decrypted_arr




        


class TestDecrypt(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().decrypt([5,7,1,4], 3), [12,10,16,13])
    
    def test2(self):
        self.assertEqual(Solution().decrypt([1,2,3,4], 0), [0,0,0,0])
    
    def test3(self):
        self.assertEqual(Solution().decrypt([2,4,9,3], -2), [12,5,6,13])

if __name__ == '__main__':
    unittest.main()
        