class Solution {
    public int search(int[] nums, int target) {
    int left = 0; 
    int right = nums.length -1; 
    int mid = left + (right-left)/2; 


    while(right > left){ 
        mid = left + (right-left)/2; 
        if(nums[mid] > nums[right]){ 
            left = mid + 1; 
        } else if(nums[mid] < nums[right]){ 
            right = mid; 
        }
    }

    int pivot = left; 
    

    if(target >= nums[pivot] && target <= nums[nums.length -1]) { 
        right =  nums.length-1;
        left = pivot;
    } else { 
        right = pivot -1;
        left = 0; 
    }

     while(right > left){ 
        mid = left + (right-left)/2; 
        if(nums[mid] > target){ 
            left = mid + 1; 
        } else if(nums[mid] < left){ 
            right = mid; 
        } 
    }

    if(nums[right] != target){
        return -1; 
    } else { 
        return right;
    }
    }
}
