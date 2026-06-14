class Solution {
    public int[] twoSum(int[] numbers, int target) {
        if(numbers == null || numbers.length == 0){
            return null;
        }


        int left = 0; 
        int right = numbers.length -1;
        while(left < right){ 
            int currSum = numbers[left] + numbers[right]; 

            if(currSum == target){ 
                return new int[] {left + 1, right + 1}; // add one since 1 based index
            }   

            else if(currSum > target) { 
                right--; 

            } else { 
                left++; 


            }
        }
        
        return null;

    }
}
