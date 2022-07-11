"""
Nama: Timothy
NIM: 1119007
"""

if __name__ == "__main__":
    p = True
    q = True
    r = p and q
    print('Truth table')
    print('proposisi: p '+'\u2227'+' q')
    print('{:5} {:5} {:5}'.format('p','q','p'+'\u2227'+'q'))
    print('{:<5} {:<5} {:<5}'.format(p, q, r))

    p = True
    q = False
    r = p and q
    print('{:<5} {:<5} {:<5}'.format(p, q, r))

    p = False
    q = True
    r = p and q
    print('{:<5} {:<5} {:<5}'.format(p, q, r))

    p = False
    q = False
    r = p and q
    print('{:<5} {:<5} {:<5}'.format(p, q, r))