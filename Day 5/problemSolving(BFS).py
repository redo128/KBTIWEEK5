graph={
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F','G'],
    'F' : ['H'],
    'G' : ['H'],
    'H' : ['G']
}
visited = []#List untuk menyimpan node yang dikunjungi
queue = [] #menambahkan queue
def dfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print (s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
#Memanggil Fungsi BFS
print("Hasil penelusuran graf menggunakan BFS: ")
dfs(visited,graph,'A')