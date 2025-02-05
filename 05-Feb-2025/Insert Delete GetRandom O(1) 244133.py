# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
       self.randoms= set()
    def insert(self, val: int) -> bool:
        a= val in self.randoms
        if(a):
            return False
        else:
           self.randoms.add(val)
           return True
    def remove(self, val: int) -> bool:
        a= val in self.randoms
        if(a):
           self.randoms.remove(val)
           return True
        else:
            return False
    def getRandom(self) -> int:
        w=list(self.randoms)
        a=random.choice(w)
        return a


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()