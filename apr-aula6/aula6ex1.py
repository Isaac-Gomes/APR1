string = input("Digite uma string: ")
letra = input("Digite a letra a ser removida: ")

i = 0
nova_string = ""
removido = False

while i < len(string):
    if string[i] == letra and not removido:
        removido = True
    else:
        nova_string += string[i]
    i += 1

print("Nova string:", nova_string)