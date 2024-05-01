n = [5, 7, 9, 25]
mplusn = [2, 8, 'NA', 'NA', 'NA', 13, 'NA', 15, 20]

for i in range(len(mplusn)):
  if mplusn[i] == 'NA':
    mplusn[i] = n[0]
    n.remove(n[0])
    
print(n)
print(mplusn)