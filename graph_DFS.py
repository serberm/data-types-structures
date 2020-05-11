#поиск в глубину

class Node:

  def __init__(self, data):
    self.data = data
    self.adjacencyList = []
    self.visited = False

class Graph_DFS:

  def dfs_print(self, startNode):
    
    print(startNode.data)
    startNode.visited = True

    for v in startNode.adjacencyList:
       if not v.visited:
         self.dfs_print(v)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')

node1.adjacencyList.append(node3)
node1.adjacencyList.append(node2)
node3.adjacencyList.append(node4)

dfs = Graph_DFS()
dfs.dfs_print(node1)
