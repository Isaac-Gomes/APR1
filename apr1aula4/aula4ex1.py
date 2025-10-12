l=[]
i=0
while i <= 150:
    if i % 3 ==0:
        l.append(i)
    i+=1    
for j in range (0, len(l)):
    print(l[j], end=', ')