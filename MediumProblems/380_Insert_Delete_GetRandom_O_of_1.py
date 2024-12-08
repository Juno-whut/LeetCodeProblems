import unittest

import random
class RandomizedSet:

    def __init__(self):
        self.my_nums = []
        self.my_set = set()

    def insert(self, val: int) -> bool:
        if val in self.my_set:
            return False
        self.my_set.add(val)
        self.my_nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.my_set:
            self.my_set.remove(val)
            self.my_nums.remove(val)
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