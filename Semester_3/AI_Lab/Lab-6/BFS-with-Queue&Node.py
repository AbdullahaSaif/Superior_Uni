# BFS with Queue & Node

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'F': ['H']
}

visited = []
queue = []

def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        
        if m == goal:
            print(f"\nGoal node {goal} found!")
            return
        
        for neighbour in graph.get(m, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print(f"BFS Search:")
bfs(visited, graph, 'A', 'E')
