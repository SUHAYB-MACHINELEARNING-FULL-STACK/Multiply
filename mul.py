'''Multiply the number 2 over the elements of the matrix '''
from random import randint
mul = lambda list : [ 2 * i for i in list ]
for i in range(randint(1,100)):
  print(f"{mul([x for x in range(randint(1,100))])}\n\n\n")
