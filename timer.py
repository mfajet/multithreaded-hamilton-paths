import nonmulti
import multi_r
import multi
import time

graph = {
    'a': ['b','c'],
    'b': ['a','c','d'],
    'c': ['a','b','d'],
    'd': ['b','c']
}

start = time.time()
nonmulti.find_all_hamiltonian_paths(graph)
end = time.time()
one = end - start
print "one thread non-recursive", one

start = time.time()
multi.find_all_hamiltonian_paths(graph)
end = time.time()
mult = end - start
print "multi thread non-recursive", mult

print mult < one


start = time.time()
nonmulti.find_paths_recursive(graph, [])
end = time.time()
one = end - start
print "one thread recursive", one

start = time.time()
multi_r.find_paths_recursive(graph, [])
end = time.time()
mult = end - start
print "multi thread recursive", mult

print mult < one
