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
    public boolean canAttendMeetings(List<Interval> intervals) {
        for(int i = 0; i < intervals.size(); i++){ 
            Interval one = intervals.get(i); 
            for(int j = i+1; j < intervals.size(); j++){ 
                Interval two = intervals.get(j); 

                if((one.start > two.start && one.start < two.end) || (one.end > two.start && one.end < two.end)){
                    return false;
                } 

                if((two.start > one.start && two.start < one.end) || (two.end > one.start && two.end < one.end)){
                    return false;
                }

                
                if(one.start == two.start || one.end == two.end){
                    return false; 
                }
            }
        }
        return true;
    }
}
