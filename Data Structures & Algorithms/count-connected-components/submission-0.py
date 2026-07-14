class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True

            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        count = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count