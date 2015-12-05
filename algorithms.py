import sys
import random
from util import *

# Run a single instance
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


if __name__ == '__main__':
	main(sys.argv[1:])
