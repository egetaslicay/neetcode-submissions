class Solution {
    public int[][] merge(int[][] intervals) {
    if(intervals.length == 0){ 
        return new int[0][0]; 
    } 
    if(intervals.length == 1){ 
        return intervals; 
    }

    Arrays.sort(intervals, (a,b)-> a[0] - b[0]); 
    List<int[]> preRes = new ArrayList<>(); 
    preRes.add(intervals[0]); 

    for(int i = 0; i < intervals.length; i++){ 
    int[] last = preRes.get(preRes.size()-1); 
    int[] curr = intervals[i]; 
    if(curr[0] <= last[1]){ 
        last[1] = Math.max(curr[1], last[1]); 
    } else { 
        preRes.add(curr); 
    }
    } 

    int[][] result = new int[preRes.size()][2]; 
    for(int i = 0; i < preRes.size(); i++){ 
        result[i] = preRes.get(i); 
    }

    return result;


    }
}
