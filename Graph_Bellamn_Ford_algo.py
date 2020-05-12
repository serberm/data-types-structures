import sys

class Node:

  def __init__(self, data):
    self.data = data
    self.visited = False
    self.predecessor = None
    self.minDistance = sys.maxsize
    self.adjacenciesList = []


class Edge:

  def __init__(self, weight, startNode, endNode):
    self.weight = weight
    self.startNode = startNode
    self.endNode = endNode


class BellmanFord:

  HAS_CYCLE = False

  def calcShortestPath(self, vertexList, edgeList, source):

    source.minDistance = 0

    #for all edges if the distance to the destination can 
    # be shortened by taking edge then updating distance and predecessor
    for i in range(1, len(vertexList)-1):
      for e in edgeList:

        u = e.startNode
        v = e.endNode
        tempDist = u.minDistance + e.weight

        if tempDist < v.minDistance:
          v.minDistance = tempDist
          v.predecessor = u

    #detect negative cycle
    for e in edgeList:

      u = e.startNode
      v = e.endNode

      if u.minDistance + e.weight < v.minDistance:
        print('Negative cycle was detected')
        self.HAS_CYCLE = True
        return

  def getShortestPath(self, targetNode):

    if not self.HAS_CYCLE:
      print('Shortest path to ', targetNode.data, " exists, distance is ", targetNode.minDistance)

      node = targetNode
      print('Path:')

      while node:
        print(node.data)
        node = node.predecessor

    else:
      print('negative cycle is present in graph...')




A = Node('A')
B = Node('B')
C = Node('C')


AB = Edge(1, A,B)
BC = Edge(1, B,C)
CA = Edge(-3, C,A)


vertexList = [A,B,C]
edgeList = [AB, BC, CA]

Graph = BellmanFord()
Graph.calcShortestPath(vertexList, edgeList, A)
Graph.getShortestPath(C)