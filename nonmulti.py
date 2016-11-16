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
    paths={}
    for vertex in g:
        used[vertex] = 0
    used[v] = 1
    n = len(g)
    DNE = False
    i=0
    counter = 0

    while len(path) < n or DNE:
        while i < len(g[v]):
            vertex = g[v][i]
            print i
            print v
            if len(path) == n:
                str_path = '-'.join(path)
                print paths
                if not (str_path in paths):
                    counter+=1
                    paths[str_path] = counter
                    path.pop()
            elif used[vertex] == 0:
                used[vertex] = 1
                path.append(vertex)
                v = vertex
                i=0
            else:
                i+=1
def find_paths_from_v(g, v):
    start = v
    n = len(g)
    paths = []
    path=[v]
    used = {}
    for vertex in g:
        used[vertex] = 0
    used[v] = 1
    count_dict = {}
    for w in g:
        count_dict[w] = 0
    while count_dict[v] < len(g[v]) or (v != start and count_dict[v] >= len(g[v])):
        print v, count_dict, path
        if v != start and count_dict[v] >= len(g[v]):
            v = path.pop()
            count_dict[v]=0
            used[v] = 0
            v = path[len(path)-1]
        else:
            vertex = g[v][count_dict[v]]
            if len(path) == n:
                str_path = '-'.join(path)
                paths.append(str_path)
                count_dict[v]=0
                used[v] = 0
                path.pop()
                v = path[len(path)-1]
                print str_path

            elif used[vertex] == 0:
                used[vertex] = 1
                path.append(vertex)
                count_dict[v]+=1
                v = vertex

            else:
                count_dict[v]+=1

        print v, count_dict[v]
    return paths

def find_all_hamiltonian_paths(g):
    all_paths = []
    for v in g:
        all_paths.append(find_paths_from_v(g, v))
    return all_paths

print find_all_hamiltonian_paths(graph)
