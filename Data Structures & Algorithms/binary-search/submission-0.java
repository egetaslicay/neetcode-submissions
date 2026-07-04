class Solution {
    public int search(int[] nums, int target) {
    int left = 0; 
    int right = nums.length-1; 
    
    while(left < right){ 
        int middle = (left + right)/2;
        if(middle == left){
            return -1;
        }
        if(nums[middle] < target){ 
            left = middle;
        } else if(nums[middle] > target){ 
            right = middle;
        } else { 
            return middle;
        }
    }

    return -1;



    }
}
