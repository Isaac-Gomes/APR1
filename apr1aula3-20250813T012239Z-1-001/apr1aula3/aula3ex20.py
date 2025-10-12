i = 0
soma = 0
while i <= 100:
    j=1
    fact = 1
    while j <= i:
        fact=fact*j
        j+=1
    soma= soma + (100-i)/fact
    i+=1
print(soma)