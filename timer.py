import nonmulti
import multi_r
import multi
import time

graph = {
    'a': ['b','c','d','e','f', 'g'],
    'b': ['a','c','d','e','f', 'g'],
    'c': ['a','b','d','e','f', 'g'],
    'd': ['a','b','c','e','f', 'g'],
    'e': ['a','b','c','d','f','g'],
    'f': ['a','b','c','d','e','g'],
    'g': ['a','b','c','d','e','f']
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
print nonmulti.r_paths

start = time.time()
multi_r.find_rec_paths(graph)
end = time.time()
mult = end - start
print "multi thread recursive", mult
print multi_r.r_paths

print mult < one
