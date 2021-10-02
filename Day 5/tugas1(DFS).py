graph={
    "A" : ["B", "E","F"],
    "B" : ["G"],
    "C" : ["D"],
    "D" : ["H"],
    "E" : ["F"],
    "F" : ["B"],
    "G" : ["C","H"],
    "H" : ["D"],
}
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
print("Hasil Penelusuran graf menggunakan DFS: ")
dfs(visited,graph,'A')