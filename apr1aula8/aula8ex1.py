def inteironegativo (n):
    try:
        n = int(n)
        if n <= 0:
            return True
        else:
            return False
    except:
        return False
def main():
    num=input('digite seu numero: ')
    if inteironegativo(num):
        print('seu numero eh um numero negativo')
    else:
        print('seu numero nao eh um numero negativo')
main()
