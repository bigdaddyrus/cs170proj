from util import *

outputfile = "nb.out"
analysis = "analysis_nb.out"

foutput = open(outputfile, "r")
fanalysis = open(analysis, "w")

direc = "instances/"

num_of_files = 100

edges_total = 0
score_total = 0
for i in xrange(num_of_files):
    solution_list = foutput.readline().split()
    filename = direc + str(i + 1) + ".in"
    fin = open(filename, "r")
    size = get_size(fin)

    matrix = parse_file_to_matrix(fin, size)
    f_edges, score = count_forward_edge_matrix_score(solution_list, matrix)
    edges_total += f_edges
    score_total += score
    print "instance {} : forward edges = {}, score = {}.".format(i+1, f_edges, score)
    fin.close()
print "total edges = {}, total score = {}.".format(edges_total, score_total)

foutput.close()
fanalysis.close()