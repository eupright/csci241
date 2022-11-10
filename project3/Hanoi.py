import timeit
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  # TODO replace pass with your base and recursive cases.
  if n == 0:
    d.push(s.pop())
  else: 
    Hanoi_rec(n-1, s, d, a)
    d.push(s.pop())
    Hanoi_rec(n-1, a, s, d)
  print(n, s, a, d)
  print()


def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=3
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")
  #Hanoi(6) runs in 0.003102 seconds
  #Hanoi(5) runs in 0.001864 seconds
  #Hanoi(4) runs in 0.000928 seconds
  #Hanoi(3) runs in 0.000589 seconds
  #Hanoi(2) runs in 0.000242 seconds
  #Hanoi(1) runs in 0.000141 seconds