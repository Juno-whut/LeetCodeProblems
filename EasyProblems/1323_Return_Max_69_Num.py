import unittest


class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        for i in range(len(str(num))):
            if str_num[i] == '6':
                str_num =str_num[:i] + '9' + str_num[i + 1:]
                return int(str_num)
        return int(str_num)
       




class TestnumJewelsInStones(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().maximum69Number(9969), 9999)
    
    def test2(self):
        self.assertEqual(Solution().maximum69Number(96969669),99969669)


if __name__ == '__main__':
    unittest.main()