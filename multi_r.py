import threading
graph = {
    'a': ['b','c'],
    'b': ['a','c','d'],
    'c': ['a','b','d'],
    'd': ['b','c']
}

r_paths = []
threads = []
#Recursive method of finding it. Might be easier to implement/convert to the threads
#that create threads themeselves.
class find_paths_recursive(threading.Thread):

    def __init__ (self, g, path):
        threading.Thread.__init__(self)
        self.g = g
        self.path = path

    def run(self):
        global r_paths
        orig = self.path
        if not self.path: #if list is empty
            for v in self.g:# Add all vertices as start of empty list
                self.path = orig[:]#original by value not by reference
                self.path.append(v)

                thread =  find_paths_recursive(self.g,self.path)
                thread.start()
                threads.append(thread)
        elif len(self.path) == len(self.g):#if length is the number of vertices
            if len(self.path) == len(set(self.path)): # if it doesn't contain duplicates
                r_paths.append('-'.join(self.path))#add it to the list of paths
            return#STOP
        else:
            v = self.path[len(self.path)-1]#Get las vertex in path
            for w in self.g[v]: #loop through vertices it's adjacent to and add them to paths
                self.path = orig[:]
                self.path.append(w)
                thread =  find_paths_recursive(self.g,self.path)
                thread.start()
                threads.append(thread)

def find_rec_paths(g):
    thread = find_paths_recursive(g,[])
    thread.start()
    threads.append(thread)
    for thread in threads:
        thread.join()
