class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCounter = Counter(nums)
        bucket = defaultdict(list)
        res = [] 

        for element, count in myCounter.items(): 
            bucket[count].append(element)

        for i in range(len(nums), -1, -1): 
            if k <= 0: 
                break 

            if i in bucket:
                res.extend(bucket[i])
                k -= len(bucket[i])

        return res 

        