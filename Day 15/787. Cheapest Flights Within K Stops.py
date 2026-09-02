class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]
            for u, v, w in flights:
                if prices[u] != float('inf') and prices[u] + w < temp[v]:
                    temp[v] = prices[u] + w
            prices = temp

        return prices[dst] if prices[dst] != float('inf') else -1
