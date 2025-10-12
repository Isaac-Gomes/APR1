string = input("Digite uma string: ")
letra = input("Digite a letra a ser removida: ")

nova_string = ""
i = 0

while i < len(string):
    if string[i] != letra:
        nova_string += string[i]
    i += 1

print("Nova string:", nova_string)