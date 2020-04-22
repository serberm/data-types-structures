class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None


class Tree:
  def __init__(self):
    self.root = None
  
  def insert(self, data):
    if not self.root:
      self.root = Node(data)
    else:
      self.__insertNode(data, self.root)
  
  def __insertNode(self, data, node):
    if not node:
      return Node(data)
    if data >= node.data:
      node.right = self.__insertNode(data, node.right)
    if data < node.data:
      node.left = self.__insertNode(data, node.left)
    return node

  def printTree(self):
    if not self.root:
      print('tree is empty')
    else:
      self.__printTreeInOrder(self.root)
  
  def __printTreeInOrder(self, node, space=0):
    space += 5
    if node.right:
      self.__printTreeInOrder(node.right, space)
    print(end=" " * space)
    print(node.data)
    if node.left:
      self.__printTreeInOrder(node.left, space)

  def delete(self, data):
    if not self.root:
      print('tree is empty')
    else:
      self.__deleteNode(data, self.root)

  def __deleteNode(self, data, node):
    if data > node.data:
      node.right = self.__deleteNode(data, node.right)
    if data < node.data:
      node.left = self.__deleteNode(data, node.left)
    if data == node.data:
      if not node.left and not node.right:
        print('node is a leaf, deleting ', node.data)
        del node
        return None
      if node.left and node.right:
        print('node has both children, deleting ', node.data)
        node.data = self.__findPredecessor(node.left)
        self.__deleteNode(node.data, node.left)
      elif node.left and not node.right:
        print('node has only left child, deleting ', node.data)
        temp = node.left
        del node
        return temp
      elif node.right and not node.left:
        print('node has only right child, deleting ', node.data)
        temp = node.right
        del node
        return temp
    return node

  def __findPredecessor(self, leftChild):
    if leftChild.right:
      return self.__findPredecessor(leftChild.right)
    else:
      return leftChild.data




myTree = Tree()
myTree.insert(10)
myTree.insert(20)
myTree.insert(5)
myTree.insert(30)
myTree.insert(15)
myTree.insert(16)
myTree.insert(14)
myTree.insert(40)
myTree.insert(35)
myTree.insert(17)
myTree.delete(16)
myTree.printTree()

