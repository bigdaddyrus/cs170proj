
import sys
import random

# By default algorithm will name the ouput file as INPUTFILE.out
def main(argv):
    if len(argv) < 2:
        print "Usage: python algoritms.py [inputfile] [algorithm]"
        return
    filename = argv[0]
    fin = open(filename, "r")
    size = get_size(fin)
    fin.close()
    outputfile = filename + ".out"
    if argv[1] == "simple_random":
        write_result(solving_through_kruskal(vertices), outputfile)

def simple_random(size):
    lst_of_nodes = []
    for i in xrange(size):
        lst_of_nodes.append(i + 1)
    random.shuffle(lst_of_nodes)
    return lst_of_nodes

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    node1 = find(vertice1)
    node2 = find(vertice2)
    if node1 != node2:
        if rank[node1] > rank[node2]:
            parent[node2] = node1
        else:
            parent[node1] = node2
            if rank[node1] == rank[node2]: rank[node2] += 1

def solving_through_kruskal(vertices):
    for vertice in vertices:
        make_set(vertice)

    maximum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

class Vertex(Object):
	def __init__(self, index):
    	self.index = index
		self.indegree = 0
		self.outdegree = 0
		self.out_vertices = []
		self.in_vertices = []

	def add_in_vertices(self, vertex):
		self.in_vertices += vertex


	def add_out_vertices(self, vertex):
		self.out_vertices += vertex