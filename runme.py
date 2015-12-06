import sys
import random
from util import *

def main(argv):
	fout = open("nb.out", "w")
	for i in range(1,622):
		fin = open("instances/" + str(i) + ".in", "r")
		length = int(fin.readline().split()[0])
		m = parse_file_to_matrix(fin, length)
		fin.close()
		v = parse_matrix_to_vertices(m, length)
		# We can change different algorithms though next line
		solution = local_search(length, m)
		print (solution)
		l = len(solution)
		for j in xrange(l):
			fout.write(str(solution[j]))
			if j == l - 1:
				fout.write("\n")
			else:
				fout.write(" ")		
	fout.close()
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


def algo_one_with_randomization(size, vertices):
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
                k.remove_out_vertex(v)

def local_search(size, matrix):
	vertices = [i+1 for i in xrange(size)]
	def permutation(v, i=0):
		if i + 1 >= len(v):
			yield v
		else:
			for j in permutation(v, i+1):
				yield j
			for k in range(i+1, len(v)):
				v[i], v[k] = v[k], v[i]
				for j in permutation(v, i+1):
					yield j
				v[i], v[k] = v[k], v[i]
	result = []
	best_score = 0
	for order in permutation(vertices):
		sol = []
		for v in order:
			sol.append(v)
		

		count = 0
		for i in xrange(size):
			for j in xrange(i + 1, size):
				if matrix[sol[i] - 1][sol[j] - 1] == 1:
					count += 1

		if count > best_score:
			best_score = count
			result = sol
		print result

	return result








def parse_file_to_matrix(fin, size):
    d = [[0 for j in range(size)] for i in range(size)]

    for r in xrange(size):
        d[r] = map(int, fin.readline().split())
    return d

def parse_matrix_to_vertices(matrix, size):
    vertices = []
    for i in xrange(size):
        v = vertex.Vertex(i+1)
        vertices.append(v)

    for row in xrange(size):
        v = vertices[row]
        for col in xrange(size):
            if matrix[row][col] == 1:
                v.add_out_vertices(vertices[col])
    return vertices


if __name__ == '__main__':
    main(sys.argv[1:])
