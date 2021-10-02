graph={
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : ['H'],
    'G' : ['H'],
    'H' : ['G']
}
visited = []#List untuk menyimpan node yang dikunjungi
queue = [] #menambahkan queue
def bfs(visited,graph,node):
    visited.append(node)
    print(node)
    print(visited)
    queue.append(node)
    print(queue)
    while queue:
        s=queue.pop(0)
        print (s,end = " ")
        for neighbour in graph[s]:
            print(neighbour)
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
#Memanggil Fungsi BFS
print("Hasil penelusuran graf menggunakan BFS: ")
#bfs(visited,graph,'A')