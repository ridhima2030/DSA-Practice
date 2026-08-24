from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            if (current_sum - k) in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
            
            prefix_sum_count[current_sum] += 1
        
        return count
