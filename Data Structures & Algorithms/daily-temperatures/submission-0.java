class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
    int[] result = new int[temperatures.length]; 

    for(int i = 0; i < temperatures.length; i++){ 
        int currTemp = temperatures[i];
        int gap = 0; 
        
        for(int j = i+1; j < temperatures.length; j++){ 
            if(temperatures[j] > temperatures[i]){ 
                gap = j - i;
                break;
            }
        }

        result[i] = gap;
    }

    return result;
    }
}
