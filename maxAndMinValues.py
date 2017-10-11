def findMaxMin(*args): 
  if (min(args)== max(args)): 
    n =[args[0]]
  else: 
    n = [min(args),max(args)] 
  return n 
print (findMaxMin(1,5,6))
