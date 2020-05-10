class Node:
  def __init__(self,character):
    self.character = character
    self.leftNode = None
    self.midNode = None
    self.rightNode = None
    self.value = 0

class TST:
  def __init__(self):
    self.root = None

  def put(self, word, number):
    self.root = self.__putRec(word, 0, self.root, number)

  def __putRec(self, word, index, node, number):

    letter = word[index]

    if not node:
      node = Node(letter)

    if letter < node.character:
      node.leftNode = self.__putRec(word, index, node.leftNode, number)
    elif letter > node.character:
      node.right = self.__putRec(word, index, node.rightNode, number)
    elif index < len(word) - 1:
      node.midNode = self.__putRec(word, index+1, node.midNode, number)
    else:
      node.value = number

    return node


myTree = TST()
myTree.put('car', 23)
myTree.put('cat', 40)
myTree.put('bat', 19)

print('done')



