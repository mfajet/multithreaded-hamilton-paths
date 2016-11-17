import nonmulti
import multi_r
import time

graph = {
    'a': ['b','c'],
    'b': ['a','c','d'],
    'c': ['a','b','d'],
    'd': ['b','c']
}

start = time.time()
nonmulti.find_paths_recursive(graph, [])
end = time.time()
print "one thread", (end - start)

start = time.time()
multi_r.find_paths_recursive(graph, [])
end = time.time()
print "multi thread", (end - start)
