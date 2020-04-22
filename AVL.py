class Node:
  def __init__(self,data):
    self.data = data
    self.height = 0
    self.right = None
    self.left = None


class AVL:
  def __init__(self):
    self.root = None

  def insert(self,data):
    self.root = self.__insertNode(data, self.root)
  
  def __insertNode(self,data,node):
    if not node:
      return Node(data)
    if node.data > data:
        node.left = self.__insertNode(data, node.left)
    else:
        node.right = self.__insertNode(data, node.right)

    node.height = max(self.__calcHeight(node.left), self.__calcHeight(node.right)) + 1

    return self.__settleViolation(data, node)
  
  def __settleViolation(self, data, node):
    balance = self.__calcBalance(node)

    if balance > 1 and data < node.left.data:
      print('left left heavy on node ', node.data)
      return self.__rotateRight(node)
    elif balance < -1 and data > node.right.data:
      print('right right heavy on node ', node.data)
      return self.__rotateLeft(node)
    elif balance > 1 and data > node.left.data:
      print('left right heavy on node ', node.data)
      node.left = self.__rotateLeft(node.left)
      return self.__rotateRight(node)
    elif balance < -1 and data < node.right.data:
      print('right left heavy on node ', node.data)
      node.right = self.__rotateRight(node.right)
      return self.__rotateLeft(node)
    
    return node

  def printGraph(self):
    if not self.root:
      print('tree is empty')
    else:
      self.printGraphRec(self.root)
  
  def printGraphRec(self, node, space = 0):
    if not node:
      return 
    space += 5
    self.printGraphRec(node.right, space)
    print(end=" " * space)
    print(node.data)
    self.printGraphRec(node.left, space)

  def printTree(self):
    if not self.root:
      print('tree is empty')
    else:
      self.printTreeRec(self.root)
  
  def printTreeRec(self, node):
    if node.left:
      self.printTreeRec(node.left)
    print(node.data, " ", end='')
    if node.right:
      self.printTreeRec(node.right)
  
  def remove(self, data):
    if not self.root:
      print('tree is empty')
    else:
      self.root = self.removeNode(data, self.root)

  def removeNode(self, data, node):
    if node.data > data:
      print('looking on left side of ', node.data)
      node.left = self.removeNode(data, node.left)
    elif  node.data < data:
      print('looking on right side of ', node.data)
      node.right = self.removeNode(data, node.right)
    else:
      if not node.left and not node.right:
        print('removing leaf node ', node.data)
        del node
        return None
      elif not node.right:
        print('target has left child ', node.left.data)
        temp = node.left
        del node
        
      elif not node.left:
        print('target has right child ', node.rihgt.data)
        temp = node.right
        del node
        return temp
      elif node.left and node.right:
        print('removing node with 2 childs....')
        temp = self.__findPredecessor(node.left)
        node.data = temp.data
        node.left = self.removeNode(temp.data, node.left)
    if not node:
      return node
    
    node.height = max(self.__calcHeight(node.right), self.__calcHeight(node.left)) + 1

    balance = self.__calcBalance(node)

    if balance > 1 and self.__calcBalance(node.left) >= 0:
      print('left left heavy on node ', node.data)
      return self.__rotateRight(node)
    elif balance < -1 and self.__calcBalance(node.right) <= 0:
      print('right right heavy on node ', node.data)
      return self.__rotateLeft(node)
    elif balance > 1 and self.__calcBalance(node.left) < 0:
      print('left right heavy on node ', node.data)
      node.left = self.__rotateLeft(node.left)
      return self.__rotateRight(node)
    elif balance < -1 and self.__calcBalance(node.right) > 0:
      print('right left heavy on node ', node.data)
      node.right = self.__rotateRight(node.right)
      return self.__rotateLeft(node)
    
    return node
  
  def __findPredecessor(self, node):
    if node.right:
      self.__findPredecessor(node.right)
    else:
      return node

  def __calcHeight(self,node):
    if not node:
      return -1
    return node.height
  
  def __calcBalance(self, node):
    if not node:
      return 0
    return self.__calcHeight(node.left) - self.__calcHeight(node.right)
  
  def __rotateRight(self, node):
    print('rotate to the right node ', node.data)
    tempLeft = node.left
    t = tempLeft.right
    tempLeft.right = node
    node.left = t
    node.height = max(self.__calcHeight(node.left), self.__calcHeight(node.right)) + 1
    tempLeft.height = max(self.__calcHeight(tempLeft.left), self.__calcHeight(tempLeft.right)) + 1

    return tempLeft

  def __rotateLeft(self, node):
    print ('rotating to the left node ', node.data)
    tempRight = node.right
    t = tempRight.left
    tempRight.left = node
    node.right = t
    node.height = max(self.__calcHeight(node.left), self.__calcHeight(node.right)) + 1
    tempRight.height = max(self.__calcHeight(tempRight.left), self.__calcHeight(tempRight.right)) + 1

    return tempRight
    
    

myTree = AVL()
myTree.insert(40)
myTree.insert(30)
myTree.insert(50)
myTree.insert(20)
myTree.insert(45)
myTree.insert(60)
myTree.insert(70)
myTree.printGraph()
myTree.remove(20)
myTree.printGraph()
    