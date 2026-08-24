class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            if current_start < prev_end:
                count += 1  
            else:
                prev_end = current_end  
                
        return count
