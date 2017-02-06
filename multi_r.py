import threading
graph = {}

global r_paths

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
                try:
                    thread =  find_paths_recursive(self.path)
                    thread.start()
                    threads.append(thread)
                except:
                    #do nothing
                    print "Error starting thread"
        elif len(self.path) == len(graph):#if length is the number of vertices
            if len(self.path) == len(set(self.path)): # if it doesn't contain duplicates
                r_paths.append('-'.join(self.path))#add it to the list of paths
            return#STOP
        else:
            v = self.path[len(self.path)-1]#Get las vertex in path
            for w in graph[v]: #loop through vertices it's adjacent to and add them to paths
                self.path = orig[:]
                self.path.append(w)
                try:
                    thread =  find_paths_recursive(self.path)
                    thread.start()
                    threads.append(thread)
                except:
                    print "Error starting thread"

def find_rec_paths(g):
    global graph
    graph = g
    thread = find_paths_recursive([])
    thread.start()
    threads.append(thread)

    for thread in threads:
        thread.join()
