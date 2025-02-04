# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:
    def __init__(self):
        count=Counter()
        frq=Counter()
        self.count=count
        self.frq=frq
    def add(self, number: int) -> None:
        a=self.count[number]
        self.count[number]+=1
        self.frq[a]-=1
        self.frq[a+1]+=1
        # return 0

    def deleteOne(self, number: int) -> None:
        a=self.count[number]
        if(a):
            self.count[number]-=1
            self.frq[a]-=1
            self.frq[a-1]+=1
        # return null
    def hasFrequency(self, frequency: int) -> bool:
        # print(self.count)
        # print(self.frq)
        a=self.frq[frequency]>=1
        return (a)
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)