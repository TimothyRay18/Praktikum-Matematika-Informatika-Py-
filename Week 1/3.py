"""
Nama: Timothy
NIM: 1119007
"""

if __name__ == "__main__":
    print('Truth table')
    print('proposisi: p '+'\u2228'+' q')
    print('{:5} {:5} {:5}'.format('p','q','p'+'\u2228'+'q'))

    p=True
    q=False

    for x in [p,q]:
        for y in [p,q]:
            print('{:<5} {:<5} {:<5}'.format(str(x),str(y),str(x or y)))