class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [] 

        counter = Counter(nums)
        lis = tuple(counter.items())

        lis = sorted(lis, key=lambda item: item[1], reverse=True)

        for i in range(k): 
            res.append(lis[i][0])

        return res


