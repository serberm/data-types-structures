class HashTable():
  def __init__(self, data):
    self.size = 10
    self.keys = [None] * self.size
    self.values = [None] * self.size

  def put(self, key, data):

    index = self.hashfunction(key)

    #not None -> it is a collision !!!!
    while self.keys[index] is not None:
      if self.keys[index] == key:
        self.values[index] = data #update
        return
      
      #rehashing, trying to find another slot
      #this is linear probing
      index = (index+1) % self.size
    
    #insert
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
        return self.values[index]

      index = (index+1) % self.size

    return None


    