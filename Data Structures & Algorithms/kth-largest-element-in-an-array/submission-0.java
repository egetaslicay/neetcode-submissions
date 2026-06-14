class Solution {
    public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(Collections.reverseOrder());

    for(int num : nums){ 
    minHeap.add(num);
    }
    int result = -1;
    for(int i = 0; i < nums.length; i++){ 
    if(i+1 == k){ 
        return minHeap.poll(); 
    }
    minHeap.poll();


    }

    return result;
    }
}
