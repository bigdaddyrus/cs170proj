from util import *

# Algorithms -------------------------------

def simple_random(size):
    lst_of_nodes = []
    for i in xrange(size):
        lst_of_nodes.append(i + 1)
    random.shuffle(lst_of_nodes)
    return lst_of_nodes


def solving_through_algo1(vertices, size):
    for i in range(size):
        if vertices[i].indegree >= vertices[i].outdegree:
            for v in vertices[i].out_vertices:
                v.indegree -= 1
                v.in_vertices.remove(vertices[i])
            vertices[i].out_vertices = None
            vertices.outdegree = 0

        else:
            for v in vertices[i].in_vertices:
                v.outdegree -= 1
                v.out_vertices.remove(vertices[i])
            vertices[i].indegree = None
            vertices.indegree = 0
    sorted(vertices, key=vertices.indegree)
    return vertices


def algo_one(vertices, size):
    l = 0
    u = size - 1
    result = [i for i in xrange(size)]
    for i in xrange(size):
        v = vertices[i]
        indegree = v.get_indegree()
        outdegree = v.get_outdegree()
        if indegree <= outdegree:
            result[l] = v
            l += 1
        else:
            result[u] = v
            u -= 1
        if u < l:
            break
    rank_of_nodes = map(lambda x: (x.get_index()), result)
    return rank_of_nodes

def algo_two(vertices, size):
	return []
