import unittest


class AllOne:

    def __init__(self):
        self.dict = {}
        self.dict_max = 0
        self.dict_min = float('inf')

    def inc(self, key: str) -> None:
        if key not in self.dict:
            self.dict[key] = 0
        self.dict[key] += 1
        if self.dict[key] > self.dict


    def dec(self, key: str) -> None:
        

    def getMaxKey(self) -> str:
        

    def getMinKey(self) -> str:
      