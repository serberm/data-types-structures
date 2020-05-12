# Shortest path algo

# Assymptotically the fastest single-source shortest-path 
# algo for arbitrary directed graph with inbounded non-negative weights

import sys, heapq

class Edge:

  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.targetVertex = targetVertex


class Node:

  def __init__(self, data):
    self.data = data
    self.visited = False
    self.predecessor = None
    self.adjacenciesList = []
    self.minDistance = sys.maxsize #basically infinity

  # override rich comparison operators for heapq operations 
  # since it compares instances with each heappush
  def __lt__(self, other):
    return self.minDistance < other.minDistance
  
  def __eq__(self, other):
    return self.minDistance == other.minDistance

  def __gt__(self, other):
    return self.minDistance > other.minDistance


class DijkstraAlgo:
  
  def calcShortestPath(self, startVertex):

    #initializing with source
    q = []
    startVertex.minDistance = 0
    heapq.heappush(q, startVertex)

    while len(q) > 0:

      #get vertex with smallest distance
      actualVertex = heapq.heappop(q)

      #looping through all neighbors
      for edge in actualVertex.adjacenciesList:
        u = edge.startVertex
        v = edge.targetVertex
        newDistance = u.minDistance + edge.weight

        #if True -> found shorter path
        if newDistance < v.minDistance:
          v.predecessor = u
          v.minDistance = newDistance
          heapq.heappush(q,v)

  def getShortestPath(self, targetVertex):

    print("For vertex ", targetVertex.data, " ,distance is ", targetVertex.minDistance)

    #backtracking from target vertex to source by predecessors
    node = targetVertex
    print('Path:')

    while node:
      print(node.data)
      node = node.predecessor





A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
M = Node('M')

AB = Edge(10, A,B)
A.adjacenciesList.append(AB)
B.adjacenciesList.append(AB)

AC = Edge(5, A,C)
A.adjacenciesList.append(AC)
C.adjacenciesList.append(AC)

BC = Edge(28, B,C)
B.adjacenciesList.append(BC)
C.adjacenciesList.append(BC)

BD = Edge(15, B,D)
B.adjacenciesList.append(BD)
D.adjacenciesList.append(BD)

CE = Edge(40, C,E)
C.adjacenciesList.append(CE)
E.adjacenciesList.append(CE)

DE = Edge(36, D,E)
D.adjacenciesList.append(DE)
E.adjacenciesList.append(DE)

CM = Edge(92, C,M)
C.adjacenciesList.append(CM)
M.adjacenciesList.append(CM)

EM = Edge(81, E,M)
E.adjacenciesList.append(EM)
M.adjacenciesList.append(EM)

Graph = DijkstraAlgo()
Graph.calcShortestPath(A)
Graph.getShortestPath(M)
