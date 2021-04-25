'''Multiply the number 2 over the elements of the matrix '''
from random import randint
mul = lambda list : [ randint(1,100) * i for i in list ]
for i in range(randint(1,100)):
  print(f"{"         ,        ".join(mul([x for x in range(randint(1,100))]))}\n\n\n")
