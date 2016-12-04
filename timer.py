import nonmulti
import multi_r
import multi
import time
import cProfile
import graphs

graph = graphs.graph5
# graph = {
#     'a': ['b','c','d','e'],
#     'b': ['a','c','d','e'],
#     'c': ['a','b','d','e'],
#     'd': ['b','c','a','e'],
#     'e': ['a', 'b', 'c', 'd']
# }

print "*************************************************************"


start = time.time()
res1 = nonmulti.find_all_hamiltonian_paths(graph)
end = time.time()
one = end - start
print "one thread non-recursive", one

start = time.time()
res2 = multi.find_all_hamiltonian_paths(graph)
end = time.time()
mult = end - start
print "multi thread non-recursive", mult
print "Same Results", sorted(res1) == sorted(res2)

print "Threaded faster?", mult < one

print """

"""


start = time.time()
nonmulti.find_rec_paths(graph)
end = time.time()
one = end - start
print "one thread recursive", one


start = time.time()
multi_r.find_rec_paths(graph)
end = time.time()
mult = end - start
print "multi thread recursive", mult
print "Same Results", sorted(multi_r.r_paths) == sorted(nonmulti.r_paths)

print "Threaded faster?", mult < one
print ""
print "Paths:", multi_r.r_paths
print "*************************************************************"
