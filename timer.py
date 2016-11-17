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
one = end - start
print "one thread", one

start = time.time()
multi_r.find_paths_recursive(graph, [])
end = time.time()
mult = end - start
print "multi thread", mult

print mult < one
