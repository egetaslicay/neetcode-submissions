class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        freq = [[] for i in range(len(nums)+1)] 

        for n in nums: 
            count[n] = 1 + count.get(n, 0)

        for key, val in count.items(): 
            freq[val].append(key)


        res = []
        for i in range(len(freq), 0, -1): 
            if len(freq[i]) != 0: 
                while k > 0 and freq[i]: 
                    res.append(freq[i].pop())
                    k =- 1

        return res



