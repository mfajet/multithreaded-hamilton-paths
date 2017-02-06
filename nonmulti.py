#Graphs will be stored as an adjacency list implemented as a dict that maps
#vertices to the vertices their adjacent to
# b----c
# | \/ |
# | /\ |
# a    d

graph = {}
#how to print all edges
def print_edges(g):
    for v in g:
        for w in g[v]:
            print "%s,%s" % (v,w)

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


#Function to find all hamiltonian paths from a certain vertex, given the graph
def find_paths_from_v(g, v):
    start = v
    n = len(g)
    paths = []
    path=[v]
    used = {}
    for vertex in g:
        used[vertex] = 0
    used[v] = 1
    count_dict = {}#Keeps all the counters for vertices
    for w in g:
        count_dict[w] = 0
    while count_dict[v] < len(g[v]) or (v != start):
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

            elif used[vertex] == 0:
                used[vertex] = 1
                path.append(vertex)
                count_dict[v]+=1
                v = vertex

            else:
                count_dict[v]+=1
    return paths

def find_all_hamiltonian_paths(g):
    all_paths = []
    for v in g:
        all_paths.append(find_paths_from_v(g, v))
    return all_paths

r_paths = []
#Recursive method of finding it. Might be easier to implement/convert to the threads
#that create threads themeselves.
def find_paths_recursive(path):
    global r_paths
    orig = path
    if not path: #if list is empty
        for v in graph:# Add all vertices as start of empty list
            path = orig[:]#original by value not by reference
            path.append(v)
            find_paths_recursive(path)
    elif len(path) == len(graph):#if length is the number of vertices
        if len(path) == len(set(path)): # if it doesn't contain duplicates
            r_paths.append('-'.join(path))#add it to the list of paths
        return#STOP
    else:
        v = path[len(path)-1]#Get las vertex in path
        for w in graph[v]: #loop through vertices it's adjacent to and add them to paths
            path = orig[:]
            path.append(w)
            find_paths_recursive(path)

def find_rec_paths(g):
    global graph
    graph = g
    find_paths_recursive([])
