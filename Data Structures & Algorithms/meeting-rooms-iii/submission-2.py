class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        freeHeap = []       # minheap with (room#)
        busyHeap = []       # minheap with (endtime of meeting, room #)
        meetingCount = defaultdict(int) # for some meeting room how many meetings occured there 
        
        meetings.sort() 


        for j in range(n):      # place all the rooms into the freeheap 
            freeHeap.append(j) 


        for i in range(len(meetings)): 
            currStart, currEnd = meetings[i] 
            
            # pop all ended meetings
            while busyHeap and busyHeap[0][0] <= currStart: 
                endTime, roomNum = heapq.heappop(busyHeap)

                # give this roomNum back to free 
                heapq.heappush(freeHeap, roomNum)

            # check if there is any free rooms 
            if freeHeap:
                # if free room then just push this meeting into the busy heap with that

                freedRoom = heapq.heappop(freeHeap)
                heapq.heappush(busyHeap, (currEnd, freedRoom))
                meetingCount[freedRoom] += 1
            else: 
                # pop the earliest ending meeting and push this meeting but make its new ending time based on its own length and the end time of the popped meeting
                endTime, roomNum = heapq.heappop(busyHeap)  
                currLength = currEnd - currStart 
                heapq.heappush(busyHeap, (endTime + currLength, roomNum))
                meetingCount[roomNum] += 1

        
        # whats the max # of meetings any room has had 
        mostMeetings = max(meetingCount.values())
        
        for i in range(n): # find the first / lowest numbered room to get have that # of meetings 
            if meetingCount[i] == mostMeetings: 
                return i 


        return -1 

