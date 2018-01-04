#
# Owen Fish
# 703-915-1306
# fish.owenc@gmail.com




from Deque import Deque

class Queue:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    #TODO replace pass with your implementation
    return str(self._dq)

  def __len__(self):
    #TODO replace pass with your implementation
    return len(self._dq)

  def enqueue(self, val):
    #TODO replace pass with your implementation
    self.push_back(val)

  def dequeue(self):
    #TODO replace pass with your implementation
    self.pop_front()

if __name__ == '__main__':
  pass #Unit tests make this unnecessary
