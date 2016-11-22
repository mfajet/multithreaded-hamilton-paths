import threading
graph = {
    'a': ['b','c','d','e'],
    'b': ['a','c','d','e'],
    'c': ['a','b','d','e'],
    'd': ['b','c','a','e'],
    'e': ['a', 'b', 'c', 'd']
}


r_paths = []
threads = []
#Recursive method of finding it. Might be easier to implement/convert to the threads
#that create threads themeselves.
class find_paths_recursive(threading.Thread):

    def __init__ (self, path):
        threading.Thread.__init__(self)
        self.path = path

    def run(self):
        global r_paths
        orig = self.path
        if not self.path: #if list is empty
            for v in graph:# Add all vertices as start of empty list
                self.path = orig[:]#original by value not by reference
                self.path.append(v)

                thread =  find_paths_recursive(self.path)
                thread.start()
                threads.append(thread)
        elif len(self.path) == len(graph):#if length is the number of vertices
            if len(self.path) == len(set(self.path)): # if it doesn't contain duplicates
                r_paths.append('-'.join(self.path))#add it to the list of paths
            return#STOP
        else:
            v = self.path[len(self.path)-1]#Get las vertex in path
            for w in graph[v]: #loop through vertices it's adjacent to and add them to paths
                self.path = orig[:]
                self.path.append(w)
                thread =  find_paths_recursive(self.path)
                thread.start()
                threads.append(thread)

# def find_rec_paths(g):
global graph
#graph = g
thread = find_paths_recursive([])
thread.start()
threads.append(thread)

for thread in threads:
    thread.join()
r_paths_2 = []
threads_2 = []
#Recursive method of finding it. Might be easier to implement/convert to the threads
#that create threads themeselves.
class find_paths_recursive_2(threading.Thread):

    def __init__ (self, g, path):
        threading.Thread.__init__(self)
        graph = g
        self.path = path

    def run(self):
        global r_paths_2
        orig = self.path
        if not self.path: #if list is empty
            for v in graph:# Add all vertices as start of empty list
                self.path = orig[:]#original by value not by reference
                self.path.append(v)

                thread =  find_paths_recursive_2(graph,self.path)
                thread.start()
                threads_2.append(thread)
        elif len(self.path) == len(graph):#if length is the number of vertices
            if len(self.path) == len(set(self.path)): # if it doesn't contain duplicates
                r_paths_2.append('-'.join(self.path))#add it to the list of paths
            return#STOP
        else:
            if len(self.path) == len(set(self.path)):
                v = self.path[len(self.path)-1]#Get las vertex in path

                for w in graph[v]: #loop through vertices it's adjacent to and add them to paths
                    self.path = orig[:]
                    self.path.append(w)
                    thread =  find_paths_recursive_2(graph,self.path)
                    thread.start()
                    threads_2.append(thread)
            else:
                return

def find_rec_paths_2(g):
    thread = find_paths_recursive_2(g,[])
    thread.start()
    threads_2.append(thread)
    for thread in threads_2:
        thread.join()
