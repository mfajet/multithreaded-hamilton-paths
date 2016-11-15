#Graphs will be stored as an adjacency list implemented as a dict that maps
#vertices to the vertices their adjacent to
graph = {
    'a': ['b','c'],
    'b': ['a','c','d'],
    'c': ['a','b','d'],
    'd': ['b','c']
}

#how to print all edges
# for v in graph:
#     for w in graph[v]:
#         print "%s,%s" % (v,w)

# It is able to find a hamilton path ending at a certain vertex.
# It hasn't been completely tested yet. It works with this specific graph example.
def find_h_path_to_v(g, v):
    used = {}
    path = [v]
    for vertex in g:
        used[vertex] = 0
    used[v] = 1
    n = len(g)
    DNE = False
    i=0

    while len(path) < n or DNE:
        while i < len(g[v]):
            vertex = g[v][i]
            print i
            print v
            if len(path) == n:
                return path
            if used[vertex] == 0:
                used[vertex] = 1
                path.append(vertex)
                v = vertex
                i=0
            else:
                i+=1

print find_h_path_to_v(graph, 'c')
