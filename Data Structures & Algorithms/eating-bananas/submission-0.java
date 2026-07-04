class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = 0;
        for(int pile : piles){ 
            max = Math.max(max, pile);
        }




        for(int speed = 1; speed <= max; speed++){ 
            long totalTime = 0; 
            for(int pile : piles){ 
                long pileTime = (long) Math.ceil( (double) pile/speed); 
                totalTime += (long) pileTime;
            }

            if(totalTime <= h){ 
                return speed;
            }
        }

        return -1;
    }
}