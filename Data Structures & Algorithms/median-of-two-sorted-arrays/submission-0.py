class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 

        if(len(nums1) > len(nums2)): 
            A = nums2
            B = nums1 

        
        left = 0 
        right = len(B)-1 

        total =  len(A) + len(B)
        half = total // 2  

        while(True): 
            mid = (left + right)//2
            j = half - mid - 2 

            Aleft = A[mid] if mid >= 0 else float("-inf")
            Aright = A[mid+1] if (mid+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            if(Bleft < A[mid+1] and Aleft < B[j+1]): 
                break
            else: 
                left = mid + 1

        if(total % 2 == 0): 
            return (max(Aleft,Bleft) + min(Aright,Bright))//2
        else: 
            return min(Aright,Bright)

        
