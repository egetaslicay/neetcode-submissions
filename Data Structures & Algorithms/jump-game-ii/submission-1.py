class Solution:
    def jump(self, nums: List[int]) -> int:
        indexToJumps = defaultdict(lambda: float('inf'))
        indexToJumps[0] = 0

        def dp(idx: int, currJumps: int) -> None: 
            if indexToJumps[idx] < currJumps: 
                return 

            indexToJumps[idx] = min(indexToJumps[idx], currJumps)

            for i in range(1, nums[idx]+1): 
                if idx + i < len(nums): 
                    dp(idx + i, currJumps + 1) 

        dp(0, 0)
        return indexToJumps[len(nums)-1]
        