from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__front = None
    self.__back = None
    self.__size = 0
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    if self.__size == 0:
      return '[ ]'
    deque_str = [None] * self.__size
    for i in range(self.__size):
      deque_str[i] = str(self.__contents[(self.__front + i) % self.__capacity])
    deque_str = ', '.join(deque_str)
    deque_str = '[ ' + str(deque_str) + ' ]'
    return deque_str
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    self.__capacity = 2 * self.__capacity
    old_contents = self.__contents
    self.__contents = [None] * self.__capacity
    for i in range(self.__size):
      self.__contents[i] = old_contents[(self.__front + i) % self.__size]
    self.__front = 0
    self.__back = self.__size - 1
    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity:
      self.__grow()
    if self.__front == None:
      self.__front = 0
      self.__back = 0
    else:
      self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
    self.__contents[self.__front] = val
    self.__size += 1
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size != 0:
      value = self.__contents[self.__front]
      self.__front = (self.__front + 1) % self.__capacity
      self.__size -= 1
      if self.__size == 0:
        self.__front = None
        self.__back = None
      return value
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__size != 0:
      return self.__contents[self.__front]
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity:
      self.__grow()
    if self.__back == None:
      self.__front = 0
      self.__back = 0
    else:
      self.__back = (self.__back + 1) % self.__capacity
    self.__contents[self.__back] = val
    self.__size += 1
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size != 0:
      value = self.__contents[(self.__back + self.__capacity) % self.__capacity]
      self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
      self.__size -= 1
      if self.__size == 0:
        self.__back = None
        self.__front = None
      return value

  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__size != 0:
      return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
  #  pass
  #ad = Array_Deque()
  #ad.push_back(2)
  #print(ad)
  #print(len(ad))
  #ad.push_front(4)
  #print(ad)
  #print(len(ad))
  #ad.push_back(92)
  #ad.push_back(87)
  #ad.push_back(23)
  #print(ad)
  #print(len(ad))
  #ad.push_front(13)
  #print(ad)
  #print(len(ad))
  #print(ad.pop_back())
  #print(ad)
  #print(len(ad))
  #print('back:', ad.peek_back())
  #print('front:', ad.peek_front())
  #print(ad)
