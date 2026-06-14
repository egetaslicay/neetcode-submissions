class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 0 || prices == null){
            return 0;
        }

    int minSF = prices[0]; 
    int maxProfit = 0;     

    for(int i = 1; i < prices.length; i++){ 
        maxProfit = Math.max(maxProfit, prices[i] - minSF);
        minSF = Math.min(prices[i], minSF);

    }

    return maxProfit;
    

    }
}
