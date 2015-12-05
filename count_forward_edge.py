import sys
from util.py import Vertex
# assumes files are well formatted
# if you have errors, make sure you double check our input and output format 
def main(argv):
	if len(argv) != 2:
		print "Usage: python scorer_single.py [path_to_instance] [path_to_answer]"
		return
	print processTest(argv[0], argv[1])



def countForwardEdge(solution_list, list_vertex):
	if len(solution_list) < 1:
		print "Invalid Solution List"
	count = 0
	i = 0
	k = 1
	for k in xrange(len(solution_list)):
		if i >= k:
			k = i + 1
		if i > len(solution_list):
			break
		if solution_list[k] in list_vertex[i].out_vertices
			count += 1
			k += 1
		i += 1
