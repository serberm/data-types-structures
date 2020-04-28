class Node:
  def __init__(self, data):
    self.data = data
    self.property = 'red'
    self.right = None
    self.left = None
    self.parent = None


class RBT:
  def __init__(self):
    self.root = None
  
  def insert(self, data):
    if not self.root:
      new_node = Node(data)
      new_node.property = 'black'
      self.root = new_node
    else:
      self.__insertNode(data, self.root, None)

  def __insertNode(self, data, node, parent):
    if not node:
      new_node = Node(data)
      new_node.parent = parent

      #case 1
      if new_node.parent.property == 'red':
        uncle = self.__getUncle(new_node)
        if uncle.property == 'red':
          print("\033[1;33;42m","Parent and Uncle are Red... recoloring on node ", new_node.data)
          new_node.parent.property = 'black'
          uncle.property = 'black'
          if self.root != new_node.parent.parent:
            print('Grandparent is not root, recoloring... ', new_node.parent.parent.data)
            new_node.parent.parent.property = 'red'
          else:
            print("\033[1;33;42m",'Grandparent is root...')

        #case 2
        if uncle.property == 'black':
          print("\033[1;33;42m","Uncle is black for node ", new_node.data)
          parent = new_node.parent
          grandparent = parent.parent
          top = grandparent.parent

          #case 2.1
          if new_node.data >= parent.data and parent.data >= grandparent.data:
            print("\033[1;33;42m", "right right heavy on grandparent ", grandparent.data)
            if top:
              if grandparent.data >= top.data:
                top.right = self.__rotateLeft(grandparent)
              else:
                top.left = self.__rotateLeft(grandparent)
            else:
              self.root = self.__rotateLeft(grandparent)

            print("\033[1;33;42m","recoloring ...")
            grandparent.property = 'red'
            parent.property = 'black'

          #case 2.2
          elif new_node.data < parent.data and parent.data >= grandparent.data:
            print("\033[1;33;42m", "right left heavy on grandparent ", grandparent.data)
            print("\033[1;33;42m", "rotating right on node ", parent.data)
            grandparent.right = new_node
            new_node.parent = grandparent

            new_node.right = parent
            parent.parent = new_node
            
            print("\033[1;33;42m", "right right heavy on grandparent ", grandparent.data)
            if top:
              if grandparent.data >= top.data:
                top.right = self.__rotateLeft(grandparent)
              else:
                top.left = self.__rotateLeft(grandparent)
            else:
              self.root = self.__rotateLeft(grandparent)
            
            parent = new_node

            print("\033[1;33;42m","recoloring ...")
            grandparent.property = 'red'
            parent.property = 'black'
            
            return None
          
          #case 2.3
          elif new_node.data < parent.data and parent.data < grandparent.data:
            print("\033[1;33;42m", "left left heavy on grandparent ", grandparent.data)
            if top:
              if grandparent.data >= top.data:
                top.right = self.__rotateRight(grandparent)
              else:
                top.left = self.__rotateRight(grandparent)
            else:
              self.root = self.__rotateRight(grandparent)

            print("\033[1;33;42m","recoloring ...")
            grandparent.property = 'red'
            parent.property = 'black'
          
          #case 2.4
          elif new_node.data >= parent.data and parent.data < grandparent.data:
            print("\033[1;33;42m", "left right heavy on grandparent ", grandparent.data)
            print("\033[1;33;42m", "rotating left on node ", parent.data)
            grandparent.left = new_node
            new_node.parent = grandparent

            new_node.left = parent
            parent.parent = new_node
            
            print("\033[1;33;42m", "left left heavy on grandparent ", grandparent.data)
            if top:
              if grandparent.data >= top.data:
                top.right = self.__rotateRight(grandparent)
              else:
                top.left = self.__rotateRight(grandparent)
            else:
              self.root = self.__rotateRight(grandparent)
            
            parent = new_node

            print("\033[1;33;42m","recoloring ...")
            grandparent.property = 'red'
            parent.property = 'black'
            
            return None

      return new_node
    if data >= node.data and not node.right:
      node.right = self.__insertNode(data, node.right, node)
    elif data < node.data and not node.left:
      node.left = self.__insertNode(data, node.left, node)
    elif data >= node.data and node.right:
      self.__insertNode(data, node.right, node)
    elif data < node.data and node.left:
      self.__insertNode(data, node.left, node)
    return node
  
  def printTree(self):
    if not self.root:
      print("\033[1;33;42m",'tree is empty')
    else:
      self.__printTreeInOrder(self.root)
  
  def __printTreeInOrder(self, node, space = 0):
    space += 5
    if node.right:
      self.__printTreeInOrder(node.right, space)
    print(end = " " * space)
    if node.property == "red":
      print( "\033[1;31;47m", node.data)
    else:
      print( "\033[1;30;47m", node.data)
    if node.left:
      self.__printTreeInOrder(node.left, space)
  
  def __rotateLeft(self,node):
    print("\033[1;33;42m",'Rotating left on node ', node.data)
    tempRight = node.right
    t = tempRight.left

    tempRight.parent = node.parent

    tempRight.left = node
    node.parent = tempRight

    node.right = t
    if t:
      t.parent = node
    
    return tempRight

  def __rotateRight(self,node):
    print("\033[1;33;42m",'Rotating right on node ', node.data)
    tempLeft = node.left
    t = tempLeft.right

    tempLeft.parent = node.parent

    tempLeft.right = node
    node.parent = tempLeft

    node.left = t
    if t:
      t.parent = node
    
    return tempLeft
  
  def __getUncle(self,node):
    grandparent = node.parent.parent
    if node.data >= grandparent.data:
      if grandparent.left:
        return grandparent.left
    else:
      if grandparent.right:
        return grandparent.right
    new_node = Node(None)
    new_node.property = 'black'
    return new_node
  





myTree = RBT()
myTree.insert(61)
myTree.insert(52)
myTree.insert(85)
myTree.insert(93)
myTree.insert(100)
myTree.insert(90)
myTree.insert(120)
myTree.insert(70)
myTree.insert(65)
myTree.insert(35)
myTree.insert(1)
myTree.insert(2)
myTree.insert(10)
myTree.insert(15)
myTree.insert(30)

myTree.printTree()
