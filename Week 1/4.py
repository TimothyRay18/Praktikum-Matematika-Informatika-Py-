"""
Nama: Timothy
NIM: 1119007
"""

if __name__ == "__main__":
    print("Truth table")
    print("proporsisi: p \u2295 q")
    print('{:5} {:5} {:5}'.format('p','q','p \u2295 q'))

    p=True
    q=False

    for x in [p,q]:
        for y in [p,q]:
            print('{:<5} {:<5} {:<5}'.format(str(x),str(y),str((x and (not y))or((not x) and y))))