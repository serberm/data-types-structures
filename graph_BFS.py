# поиск в ширину

class Node:
  def __init__(self, data):
    self.data = data
    self.adjacencyList = []
    self.visited = False
    
class Graph_BFS:
  
  def bfs_print(self, startNode):

    queue = []
    queue.append(startNode)
    startNode.visited = True

    while queue:

      actualNode = queue.pop(0)
      print('%s ' % actualNode.data)

      for neighbor in actualNode.adjacencyList:
        if not neighbor.visited:
          neighbor.visited = True
          queue.append(neighbor)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')

node1.adjacencyList.append(node3)
node1.adjacencyList.append(node2)
node3.adjacencyList.append(node4)

bfs = Graph_BFS()
bfs.bfs_print(node1)

