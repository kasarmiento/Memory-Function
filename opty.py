#!/usr/local/bin/python3

probabilities = [-1, 3/8, 3/8, 1/8, 1/8]
keys = ['','Don', 'Isabelle', 'Ralph', 'Wally']
#probabilities = [-1, 0.1, 0.2, 0.4, 0.3]
#keys = ['', 'A', 'B', 'C', 'D']
#probabilities = [-1, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]
#keys = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']


n = len(probabilities)-1
a = [[-1 for j in range(n+1)] for i in range(n+2)]
r = [[-1 for j in range(n+1)] for i in range(n+2)]

def prettyprint(a):
  for i in range(len(a)):
    print(a[i])

def A(i,j):
  result = -1

  if a[i][j] == -1:

    if j == (i-1):
      a[i][j] = 0
      result = 0

    elif j == i:

      a[i][j] = probabilities[i]
      result = probabilities[i]

    else:
      #recurrence relation
      arr=[]; sum_p=0
      for k in range(i,j+1):
        arr.append( A(i,k-1)+A(k+1,j) )
        sum_p += probabilities[k]
      result = min(arr) + sum_p

    a[i][j] = result

  else:
    result = a[i][j]

  return result




avg = A(1,n)
print(avg)
