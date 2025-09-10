# Meeting Rooms II
# Time Complexity : O(NlogN) 
# Space Complexity : O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        free_rooms = []
        if not intervals:
            return 0
        # Sort the intervals by start time
        intervals.sort(key = lambda x:x[0])
        # Create a min heap to track the minimum end time
        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0]<=i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)
