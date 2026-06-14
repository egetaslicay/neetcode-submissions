class Solution {
    public int[][] merge(int[][] intervals) {
    if (intervals.length == 0) {
    return new int[0][0];
    }
    if (intervals.length == 1) {
    return intervals;
    }    

    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    List<int[]> result = new ArrayList<>();

    result.add(intervals[0]); 

    for(int i = 1; i < intervals.length; i++){ 
    int[] last = result.get(result.size()-1); 
    int[] curr = intervals[i]; 
    if(curr[0] <= last[1]){ 
    last[1] = Math.max(curr[1], last[1]); 
    result.set(result.size()-1, last);
    } else { 
    result.add(curr); 
    }
    }

    int[][] resultA = new int[result.size()][2]; 
    for(int i = 0; i < result.size(); i++){
    resultA[i] = result.get(i);
    }

    return resultA;

    }
}
