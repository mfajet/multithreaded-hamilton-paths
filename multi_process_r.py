import multiprocessing

graph = {
    'a': ['b','c','d'],
    'b': ['a','c','d'],
    'c': ['a','b','d'],
    'd': ['b','c','a']
}

r_paths = []
#Recursive method of finding it. Might be easier to implement/convert to the threads
#that create threads themeselves.
jobs=[]
def find_paths_recursive(path):
    global jobs
    global r_paths
    orig = path
    if not path: #if list is empty
        for v in graph:# Add all vertices as start of empty list
            path = orig[:]#original by value not by reference
            path.append(v)

            proc = multiprocessing.Process(target = find_paths_recursive, args = (path,))
            jobs.append(proc)
            proc.start()
    elif len(path) == len(graph):#if length is the number of vertices
        if len(path) == len(set(path)): # if it doesn't contain duplicates
            r_paths.append('-'.join(path))#add it to the list of paths
        return#STOP
    else:
        v = path[len(path)-1]#Get las vertex in path
        for w in graph[v]: #loop through vertices it's adjacent to and add them to paths
            path = orig[:]
            path.append(w)
            proc = multiprocessing.Process(target = find_paths_recursive, args = (path,))
            jobs.append(proc)
            proc.start()
    return



proc = multiprocessing.Process(target = find_paths_recursive, args = ([],))
jobs.append(proc)
proc.start()
for job in jobs:
    job.join()
    print "job finished", job
print r_paths
