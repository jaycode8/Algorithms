
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
        for neighbours in graph[node]:
            if neighbours not in visited:
                visited.add(neighbours)


if __name__ == '__main__':
    graph = {
        "A":["B","C"],
        "B":["D","E"],
        "C":["F"],
        "D":[],
        "E":["F"],
        "F":[]
    }
    bfs(graph,'A')