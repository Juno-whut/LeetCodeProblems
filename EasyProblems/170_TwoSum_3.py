import unittest


class TwoSum:

    def __init__(self):
        self.my_map = {}
    
    def add(self, number: int) -> None:
        if number in self.my_map:
            self.my_map[number] += 1
        else:
            self.my_map.setdefault(number, 1)
        
    def find(self, value: int) -> bool:
        for i in self.my_map:
            if value-i in self.my_map:
                if value - i == i and self.my_map[i] == 1:
                    continue
                return True
        return False



if __name__ == "__main__":
    obj = TwoSum()
    obj.add(1)
    obj.add(-2)
    obj.add(3)
    obj.add(6)
    print(obj.find(4))
    print(obj.find(-1))
    print(obj.find(9))
    print(obj.find(10))
    # obj.add(0)
    # obj.add(-1)
    # obj.add(-1)
    # obj.add(0)
    # print(obj.find(0)) # true
    # print(obj.find(-1)) # true
    # print(obj.find(-2)) # true
    # print(obj.find(1)) # false
    # obj.add(3)
    # obj.add(2)
    # obj.add(1)
    # print(obj.find(2))
    # print(obj.find(3))
    # print(obj.find(4))
    # print(obj.find(5))
    # print(obj.find(6))
#    obj.add(1)
#    obj.add(2)
#    print(obj.find(1))
#    obj.add(0)
#    obj.add(0)
#    obj.add(0)
#    print(obj.find(0))

    # obj.add(1)
    # obj.add(3)
    # obj.add(5)
    # print(obj.find(4))
    # print(obj.find(7))