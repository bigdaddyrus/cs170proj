import sys
import random
import vertex

# Helper Functions ---------------------------

def get_size(file_buffer):
    first_line = file_buffer.readline()
    return int(first_line)

# Write a single result.
def write_result(result_list, outputfile):
    fout = open(outputfile, "w")
    length = len(result_list)
    for i in xrange(length):
        fout.write(str(result_list[i]))
        if i == length - 1:
            fout.write("\n")
        else:
            fout.write(" ")
    fout.close()


# Write multiple results
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


def parse_file_to_matrix(fin, size):
    d = [[0 for j in range(size)] for i in range(size)]

    for r in xrange(size):
        d[r] = map(int, fin.readline().split())
    return d


def parse_matrix_to_vertices(matrix, size):
    vertices = []
    for i in xrange(size):
        v = vertex.Vertex(i+1)
        vertices.append(v)

    for row in xrange(size):
        v = vertices[row]
        for col in xrange(size):
            if matrix[row][col] == 1:
                v.add_out_vertices(vertices[col])
    return vertices


def count_forward_edge(solution_list, vertices):
    if len(solution_list) < 1:
        print "Invalid Solution List"
    size = len(solution_list)
    count = 0
    for i in xrange(size):
        for j in xrange(i+1, size):
            if vertices[solution_list[i]-1] in vertices[solution_list[j]-1].get_in_vertex():
                count += 1
    return count

def count_forward_edge_matrix(result, d):
    ans = map(lambda x: (int(x) - 1), result)
    N = len(ans)
    count = 0
    for i in xrange(N):
        for j in xrange(i + 1, N):
            if d[ans[i]][ans[j]] == 1:
                count += 1
    return count
