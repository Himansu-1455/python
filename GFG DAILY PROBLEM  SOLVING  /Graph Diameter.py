class Solution:

    def farthestNode(self, curr, adj, currentDist, dist, visited):
        if visited[curr]:
            return
        if dist[0] < currentDist:
            # contains an array with index 0
            # having max dist and index 1 having
            # node at that distance from src
            dist[0] = currentDist
            dist[1] = curr
        visited[curr] = True
        for next_node in adj[curr]:
            if not visited[next_node]:
                self.farthestNode(next_node, adj, currentDist + 1, dist,
                                  visited)

    def diameter(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        n = len(adj) + 1
        dist = [0, 0]
        # finding node at max distance from 0th node
        self.farthestNode(0, adj, 0, dist, [False] * n)
        end1 = dist[1]

        dist = [0, 0]
        # finding node at max distance
        # from end1 of diameter
        self.farthestNode(end1, adj, 0, dist, [False] * n)
        return dist[0]
