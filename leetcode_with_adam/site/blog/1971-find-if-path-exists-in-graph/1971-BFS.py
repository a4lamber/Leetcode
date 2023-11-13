from collections import deque, defaultdict



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #  BFS
        # 1. a dict() to store node:[next_node,next_node]
        # 2. construct list() to store all whether visisted
        # 3. a dequeue() for BFS
        # 4. traversal and mark visited node if unseen
            # terminate when found

        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = [False for _ in range(n)] # n nodes in total
        seen[source] = True

        queue = deque([source])

        while queue:
            curr_node = queue.popleft()
            if curr_node == destination: return True

            for next_node in graph[curr_node]:
                # unseen or seen
                if seen[next_node] is False:
                    # mark as visited and push to the queue
                    queue.append(next_node)
                    seen[source] = True
        return False

        


# too slow to pass
        
        
