class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

    Set<List<Integer>> result = new HashSet<>();

    if(nums.length == 0 || nums == null){ 
        return new ArrayList<>(); 
    }

    Arrays.sort(nums); 
    Set<Integer> startingNum = new HashSet<>(); 


    // holy shit. thats fucked.
    for(int i = 0; i < nums.length; i++){ 
        if(!startingNum.contains(nums[i])){ 
        startingNum.add(nums[i]);
        int target = -(nums[i]); 

        int left = i+1; 
        int right = nums.length-1; 

        while(left < right){ 
            if(nums[left] + nums[right] > target){
                right--; 
            } else if(nums[left] + nums[right] < target){ 
                left++; 
            } else { 
            List<Integer> tempRes = new ArrayList<>(); 
            tempRes.add(nums[i]); 
            tempRes.add(nums[left]); 
            tempRes.add(nums[right]); 
            result.add(tempRes); 
            left++; 
            right--;
            }

        }

        }
    }

    return new ArrayList<>(result);
    







    }
}
