
class Solution:

    def safeNodes(self, V, edges):
        revAdj = [[] for _ in range(V)]
        indegree = [0] * V

        # Build reversed adjacency list
        # and compute indegree for each node
        for u, v in edges:
            revAdj[v].append(u)
            indegree[u] += 1

        q = deque()
        ans = []

        # Push all terminal nodes
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        # Kahn's Algo on reversed graph
        while q:
            curNode = q.popleft()
            ans.append(curNode)

            for prevNode in revAdj[curNode]:
                indegree[prevNode] -= 1
                if indegree[prevNode] == 0:
                    q.append(prevNode)

        # Return safe nodes
        return ans
