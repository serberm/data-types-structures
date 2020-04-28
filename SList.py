class SLNode:
   def __init__(self, value):
      self.value = value
      self.next = None

class SList:
    def __init__(self):
    	self.head = None
    def print_all(self):
      node = self.head
      while node:
        print(node.value)
        node = node.next
      return self
    def add_to_front(self, val):
      new_node = SLNode(val)
      current_head = self.head
      new_node.next = current_head
      self.head = new_node
      return self
    def add_to_back(self, val):
      new_node = SLNode(val)
      if self.head:
        runner = self.head
        while runner.next:
          runner = runner.next
        runner.next = new_node
      else:
        self.head = new_node
      return self
    def remove_from_front(self):
      self.head = self.head.next
      return self
    def remove_from_back(self):
      runner = self.head
      while runner.next.next:
        runner = runner.next
      runner.next = None
      return self
    def remove_val(self, val):
      runner = self.head
      while True:
        if runner.next == None:
          print('not found ...')
          break
        if runner.next.value == val:
          runner.next = runner.next.next
          break
        runner = runner.next
      return self
    def insert_at(self, val, index):
      runner = self.head
      while index-1:
        if runner.next == None:
          print('index out of range ...')
          break
        runner = runner.next
        index -= 1
      temp = runner.next
      runner.next = SLNode(val)
      runner.next.next = temp
      return self
    def reverse(self):
      if self.head.next:
        temp1 = self.head
        temp2 = self.head.next
        self.head = self.head.next
        self.reverse()
        temp2.next = temp1
        if temp1.next == temp2:
          temp1.next = None
      else:
        return self

my_list = SList()
for count in range(10):
  my_list.add_to_back(count)
my_list.reverse()
my_list.print_all()



