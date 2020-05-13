

#Vertex class is going to represent nodes in Graph
class Vertex:
  def __init__(self, name):
    self.name = name
    #going to assign every Node to Vertex
    self.node = None


#Node class is going to represent nodes in DisJoint set
#basically DisJoin set is a tree like structure
class Node:
  def __init__(self, height, nodeId, parentNode):
    #height is rank parameter for path compression
    self.height = height
    self.nodeId = nodeId
    self.parentNode = parentNode

class Edge:
  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.targetVertex = targetVertex

  #override comparison operators for edges
  def __lt__(self, other):
    return self.weight < other.weight
  
  def __eq__(self, other):
    return self.weight == other.weight

  def __gt__(self, other):
    return self.weight > other.weight

class DisJointSet:
  def __init__(self, vertexList):
    self.vertexList = vertexList
    #roots of the disjoint sets
    self.rootNodes = []
    #count how many nodes for disjoint sets
    self.nodeCount = 0
    self.setCount = 0
    #at the begining going to make as many sets as we have verteces
    self.makeSets(vertexList)

  def find(self, node):
    currentNode = node

    #find the root node
    while currentNode.parentNode:
      currentNode = currentNode.parentNode

    root = currentNode
    currentNode = node

    #after found the root need to do path compression
    #so with the next find() it will take only one step to fine root/representator
    while currentNode is not root:
      temp = currentNode.parentNode
      currentNode.parentNode = root
      currentNode = temp

    return root.nodeId

  def merge(self, node1, node2):
    #getting roots/representators of this nodes
    index1 = self.find(node1)
    index2 = self.find(node2)

    if index1 == index2:
      return #means they are in the same set

    #if they are in different sets then we get their root/representatives
    root1 = self.rootNodes[index1]
    root2 = self.rootNodes[index2]

    #and find higher node to make it parent of lower node
    #to compress path by rank
    #to make next find functions run faster
    if root1.height < root2.height:
      root1.parentNode = root2
    elif root1.height > root2.height:
      root2.parentNode = root1
    else:
      root2.parentNode = root1
      root1.height = root1.height + 1

  #going to assign every node to a separate set for beginning
  def makeSets(self, vertexList):
    for v in vertexList:
      self.makeSet(v)

  def makeSet(self, vertex):
    node = Node(0, len(self.rootNodes), None)
    vertex.node = node
    self.rootNodes.append(node)
    self.setCount += 1
    self.nodeCount += 1


class KruskaAlgo:

  def spanningTree(self, vertexList, edgeList):
    
    #creating a disjoint sets for all vertexes in Graph
    disJoinSet = DisJointSet(vertexList)
    spanningTree = []

    #sorting edges by weight parameter as overrided in Edge class
    #since we need to create spanning tree with min sum of edges weight
    #going to start from lightest edge to heaviest
    edgeList.sort()

    for edge in edgeList:
      u = edge.startVertex
      v = edge.targetVertex

      #check if these two verteces are in the same set
      #if they have same root/representative
      if disJoinSet.find(u.node) is not disJoinSet.find(v.node):
        spanningTree.append(edge)
        disJoinSet.merge(u.node, v.node)

    for edge in spanningTree:
      print(edge.startVertex.name, " - ", edge.targetVertex.name)




A = Vertex('A')
B = Vertex('B')
F = Vertex('F')
C = Vertex('C')
G = Vertex('G')
D = Vertex('D')
E = Vertex('E')

AF = Edge(10, A, F)
FG = Edge(5, F, G)
FC = Edge(2, F, C)
CD = Edge(1, C, D)
GD = Edge(5, G, D)
DE = Edge(4, D, E)
EB = Edge(3, E, B)
DB = Edge(3, D, B)
AD = Edge(2, A, B)
AE = Edge(5, A, E)
AC = Edge(6, A, C)

vertexList = [A, B, F, C, G, D, E]
edgeList = [AF, FG, FC, CD, GD, DE, EB, DB, AD, AE, AC]

spanningTree = KruskaAlgo()

spanningTree.spanningTree(vertexList, edgeList)

