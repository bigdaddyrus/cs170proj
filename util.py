import sys
import random

# Helper Functions ---------------------------

def get_size(file_buffer):
	first_line = file_buffer.readline()
	return int(first_line)


def write_result(result_list, outputfile):
	fout = open(outputfile, "w")
	length = len(result_list)
	for i in xrange(length):
		fout.write(str(result_list[i]))
		if i == length - 1:
			fout.write("\n")
		fout.write(" ")
	fout.close()


def write_all_results(result_lists, outputfile):
	fout = open(outputfile, "w")
	for result_list in result_lists:
		length = len(result_list)
		for i in xrange(length):
			fout.write(str(result_list[i]))
			if i == length - 1:
				fout.write("\n")
			else:
				fout.write(" ")
	fout.close()

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