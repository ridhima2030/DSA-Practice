class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def compute(expr: str) -> list[int]:
            if expr in memo:
                return memo[expr]

            res = []
            
            for i, char in enumerate(expr):
                if char in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i + 1:])

                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)

            if not res:
                res.append(int(expr))

            memo[expr] = res
            return res

        return compute(expression)
