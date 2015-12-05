from util import *

# Algorithms -------------------------------

def simple_random(size, vertices):
    lst_of_nodes = []
    for i in xrange(size):
        lst_of_nodes.append(i + 1)
    random.shuffle(lst_of_nodes)
    onward_f_edge = count_forward_edge(lst_of_nodes, vertices)
    # REVERSE THAT SHIT to get 0.5 approximation
    original = lst_of_nodes
    lst_of_nodes.reverse()
    reverse = lst_of_nodes
    reverse_f_edge = count_forward_edge(reverse, vertices)
    if onward_f_edge < reverse_f_edge:
        return reverse
    return original


def removal_algo(vertices, size):
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

# To be used by algo_two
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

def algo_one_with_randomization(vertices, size):
    l = 0
    u = size - 1
    result = [i for i in xrange(size)]
    order = []
    # Some Randomization
    for k in xrange(size):
        order.append(k)
    random.shuffle(order)
    for i in order:
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

# Pass in vertices without two-cycle, CHANGE vertices IN PLACE
def algo_two(original, size, matrix):
    vertices = parse_matrix_to_vertices(matrix, size)
    remove_two_cycles(vertices)
    random.shuffle(vertices)
    v1 = vertices[0:size/2]
    v2 = vertices[size/2:]
    # Only keep edges in v1/v2
    for v in v1:
        for o in v.get_out_vertex():
            if o in v2:
                v.remove_out_vertex(o)
        for i in v.get_in_vertex():
            if i in v2:
                i.remove_out_vertex(v)
    for v in v2:
        for o in v.get_out_vertex():
            if o in v1:
                v.remove_out_vertex(o)
        for i in v.get_in_vertex():
            if i in v1:
                i.remove_out_vertex(v)
    pi1 = algo_one(v1, len(v1))
    pi2 = algo_one(v2, len(v2))
    s1 = pi1+pi2
    s2 = pi2+pi1
    s1_f_edge = count_forward_edge(s1, original)
    s2_f_edge = count_forward_edge(s2, original)
    if s1_f_edge >= s2_f_edge:
        return s1
    return s2

def remove_two_cycles(vertices):
    size = len(vertices)
    for i in xrange(size):
        v = vertices[i]
        for k in v.get_out_vertex():
            if k in v.get_in_vertex():
                v.remove_out_vertex(k)

# To be completed
def local_search(solution, k):
    size = len(solution)
    for i in solution:
        for r in xrange(1, k+1):
            if i-r >= 0:
                swap(i-r, i, solution)
            if i+r < size:
                swap(i+r, i, solution)

def swap(a, b, l):
    l[b], l[a] = l[a], l[b]