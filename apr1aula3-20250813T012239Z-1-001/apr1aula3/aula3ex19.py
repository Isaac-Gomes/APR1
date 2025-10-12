nserie = 1000000
pi = 0
i = 0
while i < nserie:
    pi += 4 * ((-1) ** i) / (2 * i + 1)
    i += 1
print(pi)