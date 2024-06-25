#Insert Delete Get Random O(1)
import random
class RandomizedSet:
    def __init__(self):
        self.numMap = {}
        self.numList = []
        
    def insert(self, val: int) -> bool:
        res = False if val in self.numMap else True
        if res: 
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = True if val in self.numMap else False
        if res:
            val_index = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[val_index] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = val_index
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)