def inteiropositivo (n):
    if n[0]=='-' or n[0]=='+':
        try:
            n = int(n)
            if n >= 0[:1]:
                return True
            else:
                return False
        except:
            return False
    else:
        try:
            n = int(n)
            if n >= 0:
                return True
            else:
                return False
        except:
            return False
def main():
    num=input('digite seu numero: ')
    if inteiropositivo(num):
        print('seu numero eh um numero positivo')
    else:
        print('seu numero nao eh um numero positivo')
main()