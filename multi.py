import threading
graph = {
    'a': ['b','c','d','e','f','g'],
    'b': ['a','c','d','e','f','g'],
    'c': ['a','b','d','e','f','g'],
    'd': ['b','c','a','e','f','g'],
    'e': ['a', 'b', 'c', 'd','f','g'],
    'f': ['a', 'b', 'c', 'd', 'e','g'],
    'g': ['a', 'b', 'c', 'd', 'e', 'f']
}

#Function to find all hamiltonian paths from a certain vertex, given the graph
class find_paths_from_v(threading.Thread):

    def __init__ (self, g, v):
        threading.Thread.__init__(self)
        self.g = g
        self.v = v

    def run(self):
        global all_paths
        start = self.v
        n = len(self.g)
        paths = []
        path=[self.v]
        used = {}
        for vertex in self.g:
            used[vertex] = 0
        used[self.v] = 1
        count_dict = {}#Keeps all the counters for vertices
        for w in self.g:
            count_dict[w] = 0
        while count_dict[self.v] < len(self.g[self.v]) or (self.v != start):
            if self.v != start and count_dict[self.v] >= len(self.g[self.v]):
                self.v = path.pop()
                count_dict[self.v]=0
                used[self.v] = 0
                self.v = path[len(path)-1]
            else:
                vertex = self.g[self.v][count_dict[self.v]]
                if len(path) == n:
                    str_path = '-'.join(path)
                    paths.append(str_path)
                    count_dict[self.v]=0
                    used[self.v] = 0
                    path.pop()
                    self.v = path[len(path)-1]

                elif used[vertex] == 0:
                    used[vertex] = 1
                    path.append(vertex)
                    count_dict[self.v]+=1
                    self.v = vertex

                else:
                    count_dict[self.v]+=1
        all_paths.append(paths)
threads = []
all_paths = []
def find_all_hamiltonian_paths(g):
    for v in g:
        thread = find_paths_from_v(g, v)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    return all_paths
