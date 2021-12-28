class MedianFinder:

    def __init__(self):
        self._nums = []

    def addNum(self, num: int) -> None:
        self._nums.insert(self.findInsertIdx(num), num)

    def findInsertIdx(self, num):
        start_idx = 0
        end_idx = len(self._nums) - 1
        while start_idx <= end_idx:
            mid_idx = int((start_idx + end_idx) / 2)
            if self._nums[mid_idx] > num:
                end_idx = mid_idx - 1
            elif self._nums[mid_idx] < num:
                start_idx = mid_idx + 1
            else:
                return mid_idx
        return end_idx + 1

    def findMedian(self) -> float:
        if len(self._nums) % 2 == 0:
            return (self._nums[int(len(self._nums) / 2)] + self._nums[int((len(self._nums) - 1) / 2)]) / 2
        else:
            return float(self._nums[int(len(self._nums) / 2)])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

medianFinder = MedianFinder()
medianFinder.addNum(1)    #// arr = [1]
medianFinder.addNum(2)    #// arr = [1, 2]
print(medianFinder.findMedian()) #// return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)    #// arr[1, 2, 3]
print(medianFinder.findMedian()) #// return 2.0
