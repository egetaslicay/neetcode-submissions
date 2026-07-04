class Solution {
    public int climbStairs(int n) {
        // base case  since for 0, 1 and 2 stairs there is stairs amount of solutions
        if(n <= 2){ 
            return n;
        }   

        int[] dp = new int[n+1]; 
        dp[1] = 1;
        dp[2] = 2;

        for(int i = 3; i < n+1; i++){ 
            dp[n] = dp[i-1] + dp[i-2];
        }

        return dp[n];


    }
}
