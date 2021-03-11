graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop()
        print(s,end = ' -> ')

        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

bfs(visited,graph,'A')