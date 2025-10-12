n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
a = n1
b = n2
mmc = 1
i = 2

while a > 1 or b > 1:
    if a % i == 0 or b % i == 0:
        mmc *= i
        if a % i == 0:
            a //= i
        if b % i == 0:
            b //= i
    else:
        i += 1

print('MMC:', mmc)