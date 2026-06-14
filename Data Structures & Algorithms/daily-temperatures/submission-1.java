class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length]; 
        Stack<int[]> temperatureStack = new Stack<>();

        for(int i = 0; i < temperatures.length; i++){ 
            while(!temperatureStack.isEmpty() && temperatures[i] > temperatureStack.peek()[0]){ 
                int[] pair = temperatureStack.pop(); 
                result[pair[1]] = i - pair[1];
            }

            temperatureStack.push(new int[]{temperatures[i], i});
        }

        return result;



    }
}
