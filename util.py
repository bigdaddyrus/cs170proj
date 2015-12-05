import sys
import random
import vertex
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


def parse_file_to_matrix(infile):
	fin = open(infile, "r")
	N = get_size(fin)
	d = [[0 for j in range(N)] for i in range(N)]

	for r in xrange(N):
		d[r] = map(int, fin.readline().split())
	fin.close()
	return d


def parse_matrix_to_vertices(matrix, size):
	vertices = []
	for i in xrange(size):
		v = Vertex(i)
		vertices.append(v)

	for row in xrange(size):
		v = vertices[0]
		for col in xrange(size):
			if matrix[row][col] == 1:
				v.add_out_vertices(vertices[col])


