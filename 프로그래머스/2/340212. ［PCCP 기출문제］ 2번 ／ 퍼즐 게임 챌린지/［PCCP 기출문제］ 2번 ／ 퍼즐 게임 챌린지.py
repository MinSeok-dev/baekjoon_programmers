def solution(diffs, times, limit):
    def can_solve_all(level):
        total_time = 0
        prev_time = 0
        
        for i in range(len(diffs)):
            diff, time_cur = diffs[i], times[i]
            
            if diff <= level:
                total_time += time_cur
            else:
                mistakes = diff - level
                total_time += mistakes * (time_cur + prev_time) + time_cur
            
            if total_time > limit:
                return False
            
            prev_time = time_cur
        
        return total_time <= limit
    
    low, high = 1, max(diffs)
    while low < high:
        mid = (low + high) // 2
        if can_solve_all(mid):
            high = mid
        else:
            low = mid + 1
    
    return low