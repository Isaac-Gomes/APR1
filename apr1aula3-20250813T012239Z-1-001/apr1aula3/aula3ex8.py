termo = int(input('Quantos termos da sequência você vai querer? '))
fib1 = 0
fib2 = 1
i = 0

while i < termo:
    print(fib1)
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    i += 1
