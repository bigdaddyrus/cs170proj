import sys

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
        write_result(solving_through_algo1(size), outputfile)


def solving_through_algo1(vertices):
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
    sort(vertices, key = vertices.outdegree)
    return vertices
    
    
class Vertex(object):
	"""A node holds the nodes that are comming in and going out."""

	 def __init__(self, index):
	 	self.index = index
	 	self.indegree = 0
	 	self.outdegree = 0
	 	self.out_vertices = []
	 	self,in_vertices = []

	 def add_in_vertices(self, vertex):
	 	self.in_vertices += vertex

	 def add_out_vertices(self, vertex):
	 	self.out_vertices += vertex

def solving_through_kruskal(vertices):
	result = []
	l = 1
	u = size 
    for i in range(size):
    	while u != l:	
    		if vertices[i].indegree > vertices[i].outdegree:
    			result.append(vertices[i])
    			u -= 1
    		else:
    			result.append(vertices[i])
    			l += 1

    return result
    

