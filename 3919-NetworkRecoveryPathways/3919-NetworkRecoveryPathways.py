# Last updated: 7/3/2026, 12:55:39 PM
from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            costs.append(w)

        # Topological order
        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        costs = sorted(set(costs))

        def check(x):
            INF = float("inf")
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, w in graph[u]:
                    if w < x:
                        continue
                    if v != n - 1 and v != 0 and not online[v]:
                        continue
                    if dp[u] + w < dp[v]:
                        dp[v] = dp[u] + w

            return dp[n - 1] <= k

        lo, hi = 0, len(costs) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans