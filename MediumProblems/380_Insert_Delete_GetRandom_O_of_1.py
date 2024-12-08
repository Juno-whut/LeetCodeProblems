import unittest

import random
class RandomizedSet:

    def __init__(self):
        self.my_nums = []
        self.my_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.my_dict:
            return False
        self.my_nums.append(val)
        self.my_dict[val] = len(self.my_nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.my_dict and val == self.my_nums[-1]:
            del self.my_dict[val]
            self.my_nums.pop()
            return True
        elif val in self.my_dict:
            index_of_val = self.my_dict[val]
            self.my_nums[index_of_val] = self.my_nums[-1]
            self.my_dict[self.my_nums[-1]] = index_of_val
            del self.my_dict[val]
            self.my_nums.pop()
            return True
            
        return False

    def getRandom(self) -> int:
        return random.choice(self.my_nums)




class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(RandomizedSet(), None)
        self.assertTrue(RandomizedSet().insert(1), True)
        self.assertTrue(RandomizedSet().remove(2), False)
        self.assertTrue(RandomizedSet().insert(2), True)
        self.assertEqual(RandomizedSet().getRandom(), 2)
        self.assertTrue(RandomizedSet().remove(1), True)
        self.assertTrue(RandomizedSet().insert(2), True)
        self.assertEqual(RandomizedSet().getRandom(), 2)
    

    def test2(self):
        self.assertEqual(RandomizedSet(), None)
        self.assertTrue(RandomizedSet().insert(1), True)
        self.assertTrue(RandomizedSet().remove(1), True)
        self.assertTrue(RandomizedSet().insert(1), True)
        self.assertEqual(RandomizedSet().getRandom(), 1)
        self.assertTrue(RandomizedSet().remove(1), True)
    

if __name__ == "__main__":
    unittest.main()