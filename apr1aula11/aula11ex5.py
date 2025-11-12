def caracter_string(string,k):
    try:
        a = string[k]
        return caracter_string(string,k+1)
    except:
        return k
string = input('digite uma string')
cont = 0 
print(caracter_string(string, cont))   