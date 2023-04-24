def transpose(a):
  result = [[0 for i in range(len(a))] for j in range(len(a[0]))]
  for i in range(len(a)):
    for j in range(len(a[0])):
      result[j][i] = a[i][j]
  return result

def mult(a,b):
  result = [[0 for i in range(len(b[0]))] for j in range(len(a))]
  for i in range(len(a)):
   for j in range(len(b[0])):
       for k in range(len(b)):
           result[i][j] += a[i][k] * b[k][j]
  return result

def invert(a):
  n = len(a)
  result = [[0 for i in range(n)] for j in range(n)]
  
  for i in range(n):
    for j in range(n):
      if i==j:
        result[i][j] = 1
  
  for i in range(n):
    if a[i][i]==0:
      for j in range(i+1, n):
        if a[j][i]!=0:
          a[i],a[j] = a[j],a[i]
          result[i],result[j] = result[j],result[i]
  
  indices = list(range(n)) 
  
  for d in range(n):
      dScale = 1.0 / a[d][d]
      for j in range(n):
        a[d][j] *= dScale
        result[d][j] *= dScale
      for i in indices[0:d] + indices[d+1:]: 
        cScale = a[i][d] 
        for j in range(n): 
          a[i][j] = a[i][j] - cScale * a[d][j]
          result[i][j] = result[i][j] - cScale * result[d][j]
  return result
