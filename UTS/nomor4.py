"""
Nama:Timothy
NIM:1119007
"""
import random
if __name__ == "__main__":
    list_val = [True, False]
    list_operator = ['and', 'or', 'xor']
    random_p = random.choice(list_val)
    random_q = random.choice(list_val)
    random_operator = random.choice(list_operator)
    print('p: ',end='')
    print(str(random_p))
    print('q: ',end='')
    print(str(random_q))
    print()

    hasil = random_p ^ random_q

    cek = False
    while(cek==False):
        answer = input('p '+random_operator+' q = ? ')
        if(answer==str(hasil)):
            cek=True
            print('Benar')
        else:
            print('Salah')