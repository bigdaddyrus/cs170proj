
class Vertex:

    def __init__(self, index):
        self.index = index
        self.indegree = 0
        self.outdegree = 0
        self.out_vertices = []
        self.in_vertices = []

    def get_index(self):
        return self.index

    def get_indegree(self):
        return self.indegree

    def get_outdegree(self):
        return self.outdegree

    def add_indegree(self):
        self.indegree += 1

    def add_outdegree(self):
        self.outdegree += 1

    def get_out_vertex(self):
        return self.out_vertices

    def get_in_vertex(self):
        return self.in_vertices

    def add_in_vertices(self, vertex):
        self.in_vertices.append(vertex)
        self.add_indegree()

    def add_out_vertices(self, vertex):
        self.out_vertices.append(vertex)
        vertex.add_in_vertices(self)
        self.add_outdegree()