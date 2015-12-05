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
		write_result(simple_random(size), outputfile)


# Algorithms -------------------------------

def simple_random(size):
	lst_of_nodes = []
	for i in xrange(size):
		lst_of_nodes.append(i + 1)
	random.shuffle(lst_of_nodes)
	return lst_of_nodes


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


if __name__ == '__main__':
	main(sys.argv[1:])
