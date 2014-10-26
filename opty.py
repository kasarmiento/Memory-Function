#!/usr/local/bin/python3

probabilities = [None, 3/8, 3/8, 1/8, 1/8]
keys = ['','Don', 'Isabelle', 'Ralph', 'Wally']
#probabilities = [None, 0.1, 0.2, 0.4, 0.3]
#keys = ['', 'A', 'B', 'C', 'D']
#probabilities = [None, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]
#keys = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']


# n = the number of elements in the binary search tree
# a = the 2d backing array used to store calculated solutions
# r = the 2d array whos element in [i,n] would contain the optimal root
n = len(probabilities)-1
a = [[None for j in range(n+1)] for i in range(n+2)]
r = [[None for j in range(n+1)] for i in range(n+2)]


# Pretty Print: A function used to help me test my data.
# This function prints the elements of an array.
# Very useful for printing easy-to-read 2d arrays.
def prettyprint(a):
  for i in range(1,len(a)):
    print(a[i])

# A(i,j): A recursive memory function used to calculate
# a the minimum average number of comparisons for an optimal
# binary search tree. This function alters the backing array
# a[][] and the optimal root array r[][].
def A(i,j):
  result = None
  if a[i][j] == None:
    if j == (i-1):
      a[i][j] = 0
      r[i][j] = 0
      result = 0
    elif j == i:
      a[i][j] = probabilities[i]
      r[i][j] = i
      result = probabilities[i]
    else:
      #recurrence relation
      sumP = 0
      minvals = []
      kvalues = []
      for k in range(i,j+1):
        kvalues.append(k)
        minvals.append(A(i,k-1)+A(k+1,j))
        sumP += probabilities[k]
      result = min(minvals) + sumP
      index = minvals.index(min(minvals))
      r[i][j] = kvalues[index]
      a[i][j] = result
  else:
    result = a[i][j]
  return result

# Tree(i,j): This recursive function is used to print
# the arrangement of a binary search tree using parenthesis
# to distinguish between different levels of the tree.
def tree(i,j):
  s = ''
  key = ''
  root = r[i][j]
  if root == 0: #leaf
    s += ''
  elif i == j: #probabilities
    key = keys[root]
    s += key
  else: #everything else
    key = keys[root]
    s += key
    s += '('
    s += tree(i,root-1)
    s += ','
    s += tree(root+1,j)
    s += ')'
  return s

print(A(1,n))
print(tree(1,n))
