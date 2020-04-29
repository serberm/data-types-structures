CAPACITY = 15

class HeapMax():
  def __init__(self):
    self.heap = [0]*CAPACITY
    self.heap_size = 0

  def insert(self, data):
    if CAPACITY == self.heap_size:
      return 
    
    self.heap[self.heap_size] = data
    self.heap_size += 1

    self.__fix(self.heap_size-1)

  def __fix(self, index):
    parent_index = (index-1)//2

    if index > 0 and self.heap[index]>self.heap[parent_index]:
      self.__swap(index, parent_index)
      self.__fix(parent_index)

  def __swap(self, child, parent):
    temp = self.heap[child]
    self.heap[child] = self.heap[parent]
    self.heap[parent] = temp
    return
  
  def printArr(self):
    print('Heap: ' ,self.heap)

  def printTreeHorizontal(self):
    space = 40
    check = 0
    power = 0
    for index in range(0, len(self.heap)):
      check = pow(2,power)
      if index+1 == check:
        power += 1
        space //= 2
        space += space//2
        print('\n')
      
      if not power%2:
        if not index%2:
          temp = space //2
          print(end=" " * temp)
        else:
          print(end=" " * space)
      else:
        temp1 = space + 2
        print(end=" " * temp1)

      print(self.heap[index], end="")

  def printTreeVertical(self):
    if self.heap[0] == 0:
      print('Heap is empty')
    else:
      self.__printTreeVerticalRec(0)

  def __printTreeVerticalRec(self, index, space = 0):
    right_child = 2 * index + 2
    left_child = 2 * index + 1
    space += 5

    if right_child < CAPACITY:
      self.__printTreeVerticalRec(right_child, space)

    print(end=" " * space)
    print(self.heap[index])

    if left_child < CAPACITY:
      self.__printTreeVerticalRec(left_child, space)

  #peek
  def getMax(self):
    return self.heap[0]

  def __poll(self):
    max = self.getMax()

    self.heap[0] = 0
    self.heap_size -= 1

    self.__fixDown()
    return max

  def __fixDown(self, index = 0):
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if self.heap[left_child] > self.heap[right_child]:

      if self.heap[index] < self.heap[left_child]:
        self.__swap(index, left_child)
        self.__fixDown(left_child)

      else:
        return
    
    else:

      if self.heap[index] < self.heap[right_child]:
        self.__swap(index, right_child)
        self.__fixDown(right_child)

      else:
        return
  
  def heapSort(self):

    size = self.heap_size

    for index in range(0, size):
      
      max = self.__poll()
      print(max)




  
myHeap = HeapMax()
myHeap.insert(10)
myHeap.insert(20)
myHeap.insert(13)
myHeap.insert(33)
myHeap.insert(80)
myHeap.heapSort()
