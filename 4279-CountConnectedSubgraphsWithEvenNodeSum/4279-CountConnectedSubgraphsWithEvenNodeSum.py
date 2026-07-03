# Last updated: 7/3/2026, 12:55:01 PM
class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        count = 0
        
        for mask in range(1, 1 << n):
            node_sum = 0
            for i in range(n):
                if mask & (1 << i):
                    node_sum += nums[i]
            
            if node_sum % 2 != 0:
                continue
            
            if self.is_connected(mask, edges, n):
                count += 1
        
        return count
    
    def is_connected(self, mask, edges, n):
        nodes_in_mask = []
        for i in range(n):
            if mask & (1 << i):
                nodes_in_mask.append(i)
        
        if len(nodes_in_mask) == 0:
            return False
        
        adj = {node: [] for node in nodes_in_mask}
        
        for u, v in edges:
            if (mask & (1 << u)) and (mask & (1 << v)):
                adj[u].append(v)
                adj[v].append(u)
        
        visited = set()
        stack = [nodes_in_mask[0]]
        visited.add(nodes_in_mask[0])
        
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return len(visited) == len(nodes_in_mask)