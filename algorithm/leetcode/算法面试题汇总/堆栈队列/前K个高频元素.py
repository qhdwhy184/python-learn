from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            count_dict[num] += 1
        num_lst = []
        for num in count_dict:
            num_lst.append((num, count_dict[num]))
        res = sorted(num_lst, key=lambda x: x[1], reverse=True)
        return [res[i][0] for i in range(0, k)]


print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))
print(Solution().topKFrequent([1,1,1,2,2,3], 3))
print(Solution().topKFrequent([1,1,1,2,2,3], 1))
print(Solution().topKFrequent([3,0,1,0], 1))