graph={
    'A' : ['B','C'],
    'B' : ['C','D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : ['H'],
    'G' : ['H'],
    'H' : ['G']
}
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node) 
        visited.add(node)
        for neighbour in graph[node]:
            print("CARI")
            print(neighbour)
            dfs(visited,graph,neighbour)
print("Hasil Penelusuran graf menggunakan DFS: ")
dfs(visited,graph,'A')
# dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
# print(dataScientist)
# dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
# print(dataScientist)