import nonmulti
import multi_r
import multi
import time

graph = {
    'a': ['b','c','d','e'],
    'b': ['a','c','d','e'],
    'c': ['a','b','d','e'],
    'd': ['b','c','a','e'],
    'e': ['a', 'b', 'c', 'd']
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
nonmulti.find_paths_recursive([])
end = time.time()
one = end - start
print "one thread recursive", one
print nonmulti.r_paths

start = time.time()
multi_r.find_paths_recursive([])
end = time.time()
mult = end - start
print "multi thread recursive", mult
print multi_r.r_paths

print mult < one
