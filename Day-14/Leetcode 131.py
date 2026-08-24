class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int):
            # Base case: reached the end of the string
            if start == len(s):
                res.append(list(path))
                return
            
            # Explore all possible substrings starting at `start`
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    path.append(sub)        # Choose
                    backtrack(end)          # Explore
                    path.pop()              # Backtrack

        backtrack(0)
        return res
