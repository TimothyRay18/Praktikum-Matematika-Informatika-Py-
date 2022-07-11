"""
Nama:Timothy
NIM:1119007
"""

def implies(a, b):
    return (not a) or b

if __name__ == "__main__":
    print("Truth table")
    print("proporsisi: p \u21d2 q")
    print('{:5} {:5} {:5}'.format('p','q','p \u21d2 q'))

    p=True
    q=False

    for x in(p,q):
        for y in(p,q):
            print('{:<5} {:<5} {:<5}'.format(str(x),str(y),str(implies(x, y))))