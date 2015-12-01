import sys
import random

def main(argv):
	if len(argv) < 2:
                print "Usage: python instance_generator.py [size] [path_to_outputfile] [edge_probability]"
                return
        print generate_instance(argv[0], argv[1], argv[2])

def generate_instance(size, filename, seed=0.5):
	lst = [0, 1]
	N = int(size)
	if N < 1 or N > 100:
		return "N must be an integer between 1 and 100, inclusive."
	fout = open(filename, "w")
	# Line 1 must contain a single integer.
	fout.write(size)
	fout.write("\n")
	for i in xrange(N):
		for j in xrange(N):
			# A node cannot have an edge to itself.
			if i == j:
				fout.write("0")
			else:
				x = random.uniform(0, 1)
				if x <= float(seed):
					fout.write("1")
				else:
					fout.write("0")
			if j == (N - 1):
				fout.write("\n")
			else:
				fout.write(" ")
	fout.close()
	return "Finish Generating Instance"

if __name__ == '__main__':
	main(sys.argv[1:])
