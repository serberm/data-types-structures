class HashTable():
  def __init__(self):
    self.size = 10
    self.keys = [None] * self.size
    self.values = [None] * self.size

  def put(self, key, data):

    index = self.hashfunction(key)

    #not None -> it is a collision !!!!
    while self.keys[index] is not None:
      if self.keys[index] == key:
        print('key already generated, updating ......')
        self.values[index] = data #update
        return
      
      #rehashing, trying to find another slot
      #this is linear probing
      print('Re Hashing ......')
      index = (index+1) % self.size
    
    #insert
    print('Inserting ......')
    self.keys[index] = key
    self.values[index] = data

  def hashfunction(self, key):
    sum = 0
    for pos in range(len(key)):
      sum += ord(key[pos])
    
    return sum % self.size

  def get(self, key):

    index = self.hashfunction(key)

    while self.keys[index] is not None:
      if self.keys[index] == key:
        print('value found:  ', self.values[index])
        return self.values[index]

      print('Re Hashing ......')
      index = (index+1) % self.size

    print('key is not present ....')
    return None

  def printAll(self):
    print('keys ...')
    print(self.keys)
    print('values ...')
    print(self.values)

myTable = HashTable()
myTable.put('pidr',10)
myTable.put('gnida',20)
myTable.put('rdip',30)
myTable.put('drip',40)
print('_______________')
myTable.get('drip')

myTable.printAll()


    