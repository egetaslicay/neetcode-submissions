/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
    if(intervals.size() == 0){
        return 0; 
    } if(intervals.size() == 1){
        return 1;
    }

    int result = 0; 
    int currCount = 0; 

    PriorityQueue<Integer> endTimes = new PriorityQueue<>(); 
    endTimes.add(intervals.get(0).end); 
    currCount++; 
    

    for(int i = 1; i < intervals.size(); i++){ 
        if(endTimes.peek() < intervals.get(i).start){ 
        endTimes.add(intervals.get(i).end);
        currCount++;
        result = Math.max(result, currCount);
        } else { 
        endTimes.poll(); 
        endTimes.add(intervals.get(i).end);
        }
    }

    return result;
    }
}
