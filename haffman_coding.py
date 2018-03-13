# Question: Given Element and its frequency, Build a haffman tree
# Source: https://practice.geeksforgeeks.org/problems/huffman-encoding/0
# Algorithm explanation: https://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/

import heapq
class Node(object):
  def __init__(self, data=None, freq=None, left=None, right=None):
    self.data = data
    self.freq = freq
    if freq == None:
      self.freq = left.freq + right.freq
    self.left = left
    self.right = right

  def __eq__(self, other):
    return bool(self.freq == other.freq)
  def __le__(self, other):
    return bool(self.freq <= other.freq)
  def __ge__(self, other):
    return bool(self.freq >= other.freq)
  def __ne__(self, other):
    return bool(self.freq != other.freq)
  def __lt__(self, other):
    return bool(self.freq < other.freq)
  def __gt__(self,other):
    return bool(self.freq > other.freq)
    
  def __cmp__(self, other):
    return self.freq-other.freq

  def __repr__(self):
    return "(%s, %s)" % (self.freq, self.data)

def pre_order(root, haffman_code, track_traverse):
  if root:
    if not root.left or not root.right:
      haffman_code.append(track_traverse)
    pre_order(root.left, haffman_code, track_traverse+"0")
    pre_order(root.right, haffman_code, track_traverse+"1")

for _ in range(int(input())):
  arr = [s for s in str(input())]
  freq = [int(f) for f in str(input()).split(' ') if f.isdigit()]
  priority_q = [Node(d, f) for d, f in zip(arr, freq)]
  heapq.heapify(priority_q)

  while(len(priority_q)>1):
    a = heapq.heappop(priority_q)
    b = heapq.heappop(priority_q)
    c = Node(left=a,right=b)
    heapq.heappush(priority_q, c)  
  haffman_code = []
  pre_order(priority_q[0],haffman_code,"")
  print (" ".join(haffman_code))
