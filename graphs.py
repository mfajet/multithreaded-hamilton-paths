graph1 = {
    'a': ['b','c','d'],
    'b': ['a','c','d'],
    'c': ['a','b','d'],
    'd': ['b','c','a']
}

graph2 =  {
    'a': ['b','c','d','e','f','g'],
    'b': ['a','c','d','e','f','g'],
    'c': ['a','b','d','e','f','g'],
    'd': ['b','c','a','e','f','g'],
    'e': ['a', 'b', 'c', 'd','f','g'],
    'f': ['a', 'b', 'c', 'd', 'e','g'],
    'g': ['a', 'b', 'c', 'd', 'e', 'f']
}

graph3 = {
    'a': ['b','c'],
    'b': ['a','c','d'],
    'c': ['a','b','d'],
    'd': ['b','c']
}

#largest hamiltonian graph that won't give errors
graph6 = {
    'a': ['b','c','d','e'],
    'b': ['a','c','d','e'],
    'c': ['a','b','d','e'],
    'd': ['b','c','a','e'],
    'e': ['a', 'b', 'c', 'd']
}

#smallest hamiltonian graph of k3 that isn't too fast
graph5 = {
    'a' : ['b', 'c'],
    'b' : ['a', 'c'],
    'c': ['a', 'b']
}

#non-hamiltonian graph
graph6 = {
    'a' : ['b'],
    'b' : ['c', 'e'],
    'c' : ['b', 'd', 'e'],
    'd' : ['c', 'e'],
    'e' : ['b', 'd']
}

#k6 graph. Too large.
graph7 = {
    'a' : ['b', 'c', 'd', 'e', 'f'],
    'b' : ['a', 'c', 'd', 'e', 'f'],
    'c' : ['a', 'b', 'd', 'e', 'f'],
    'd' : ['a', 'b', 'c', 'e', 'f'],
    'e' : ['a', 'b', 'c', 'd', 'f'],
    'f' : ['a', 'b', 'c', 'd', 'e']
}
