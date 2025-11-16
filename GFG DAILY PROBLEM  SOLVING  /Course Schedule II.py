class Solution:

    def findOrder(self, n, prerequisites):

        # Initialize graph and in-degree array
        adj = [[] for _ in range(n)]
        inDegree = [0] * n

        # Build the graph
        for dest, src in prerequisites:
            adj[src].append(dest)
            inDegree[dest] += 1

        # Initialize the queue with
        # courses having in-degree 0
        q = deque([i for i in range(n) if inDegree[i] == 0])

        order = []

        # Process nodes with BFS
        while q :
            current = q.popleft()
            order.append(current)

            # Reduce in-degree for neighbors
            for neighbor in adj[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)

        # Check if the topological sort
        # is possible (i.e., no cycle)
        if len(order) == n:
            return order

        return []
