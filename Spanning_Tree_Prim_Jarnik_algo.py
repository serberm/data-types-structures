import heapq

class Vertex:
  def __init__(self, data):
    self.data = data
    self.visited = False
    self.adjacencyList = []

  def __str__(self):
    return self.data

class Edge:
  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.targetVertex = targetVertex

  def __lt__(self, other):
    return self.weight < other.weight

class Prims_Jarnik:
  def __init__(self, unvisitedList):
    self.unvisitedList = unvisitedList
    self.spanningTree = []
    self.edgeHeap = []
    self.fullCost = 0
  
  def calcSpanningTree(self, vertex):

    self.unvisitedList.remove(vertex)

    while self.unvisitedList:

      for edge in vertex.adjacencyList:
        if edge.targetVertex in self.unvisitedList:
          heapq.heappush(self.edgeHeap, edge)

      minEdge = heapq.heappop(self.edgeHeap)

      if minEdge.targetVertex in self.unvisitedList:
        self.spanningTree.append(minEdge)
        self.fullCost += minEdge.weight
        vertex = minEdge.targetVertex
        self.unvisitedList.remove(vertex)
      
    print('tree weight: ', self.fullCost)

    for edge in self.spanningTree:
      print(edge.startVertex, ' - ', edge.targetVertex)

A = Vertex('A')
B = Vertex('B')
E = Vertex('E')
D = Vertex('D')
G = Vertex('G')
F = Vertex('F')
C= Vertex('C')

#copy edges for both start vertext and target vertex
#to represent undirected Graph
AB = Edge(2, A, B)
BA = Edge(2, B, A)
A.adjacencyList.append(AB)
B.adjacencyList.append(BA)
BE = Edge(3, B, E)
EB = Edge(3, E, B)
B.adjacencyList.append(BE)
E.adjacencyList.append(EB)
ED = Edge(4, E, D)
DE = Edge(4, D, E)
E.adjacencyList.append(ED)
D.adjacencyList.append(DE)
DG = Edge(5, D, G)
GD = Edge(5, G, D)
D.adjacencyList.append(DG)
G.adjacencyList.append(GD)
GF = Edge(3, G, F)
FG = Edge(3, F, G)
G.adjacencyList.append(GF)
F.adjacencyList.append(FG)
FC = Edge(2, F, C)
CF = Edge(2, C, F)
F.adjacencyList.append(FC)
C.adjacencyList.append(CF)
AC = Edge(6, A, C)
CA = Edge(6, C, A)
A.adjacencyList.append(AC)
C.adjacencyList.append(CA)
BD = Edge(3, B, D)
DB = Edge(3, D, B)
B.adjacencyList.append(BD)
D.adjacencyList.append(DB)
DC = Edge(1, D, C)
CD = Edge(1, C, D)
D.adjacencyList.append(DC)
C.adjacencyList.append(CD)
FA = Edge(10, F, A)
AF = Edge(10, F, A)
F.adjacencyList.append(FA)
A.adjacencyList.append(AF)

vertexList = [A,B,E,D,G,F,C]
  
spanningTree = Prims_Jarnik(vertexList)  
spanningTree.calcSpanningTree(D)   


  