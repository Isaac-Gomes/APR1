def receberstring():
    str = input('digite sua string: ')
    return str

def main ():
    str1 = receberstring()
    str2 = receberstring()
    anagrama(str1,str2)
    if anagrama(str1, str2):
        print('True')
    else:
        print('False')
def anagrama(str1,str2):
    if len(str1) == len(str2):
        anagrama = True
        i = 0
        while i < len(str1) and anagrama:
            cont_str1 = 0 #conta qtas vezes a letra aparece em str1
            cont_str2 = 0 #conta qtas vezes a letra aparece em str2
            #conta o total de vezes que a letra da posição i de str1
            #se repete na mesma string
            for j in range(len(str1)): 
                if str1[i] == str1[j]:
                    cont_str1+=1
            #conta o total de vezes que a letra da posição i de str1
            #ocorre em str2
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    cont_str2+=1
            if cont_str1 != cont_str2:
                anagrama = False
            i+=1
        if anagrama:
            return True
        else:
            return False
        
main()