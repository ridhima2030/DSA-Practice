class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        def backtrack(start: int, current_path: list[int]):
            result.append(list(current_path))
            
            for i in range(start, len(nums)):
                # Skip duplicate elements at the same decision level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                current_path.append(nums[i])
                backtrack(i + 1, current_path)
                current_path.pop()
                
        backtrack(0, [])
        return result
