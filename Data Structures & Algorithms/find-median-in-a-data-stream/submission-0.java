class MedianFinder {

    public List<Integer> nums;

    public MedianFinder() {

    nums = new ArrayList<>();

    }
    
    public void addNum(int num) {
        nums.add(num); 
        Collections.sort(nums); 
    }
    
    public double findMedian() {
       
        if((nums.size() % 2) != 0){ 
            int index = (nums.size() - 1)/2;
            return (double) nums.get(index); 
        } else { 
            int midOne = nums.size()/2; 
            int midTwo = midOne -1; 

            double median = (double) (nums.get(midOne) + nums.get(midTwo))/2; 
            return median;
        }
    }
}
