import sys
import random
from util import *

# Algorithms -------------------------------

def simple_random(size):
	lst_of_nodes = []
	for i in xrange(size):
		lst_of_nodes.append(i + 1)
	random.shuffle(lst_of_nodes)
	return lst_of_nodes

