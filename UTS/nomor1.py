"""
Nama:Timothy
NIM:1119007
"""
import random
if __name__ == "__main__":
    list_val = [True,False]
    p = random.choice(list_val)
    q = random.choice(list_val)

    print('p: '+str(p))
    print('q: '+str(q))

    operator = input('Masukan operator (and, or, xor): ')
    print('p '+operator+' q= ')
    if(operator == 'and'):
        print(str(p and q))
    elif(operator == 'or'):
        print(str(p or q))
    else:
        print(str(p ^ q))