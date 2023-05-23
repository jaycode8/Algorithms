

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

if __name__ == '__main__':
    graph = {
        "A":["B","C"],
        "B":["D","E"],
        "C":["F"],
        "D":[],
        "E":["F"],
        "F":[]
    }
    dfs(graph,'F')