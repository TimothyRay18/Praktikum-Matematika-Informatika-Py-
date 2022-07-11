"""
Nama:Timothy
NIM:1119007
"""

def iff(a, b):
    return (a and b) or (not a and not b)

def boolean_to_tf(c):
    if c == True:
        return 'T'
    else:
        return 'F'

if __name__ == "__main__":
    print("Truth table")
    print("proporsisi: p \u21d2 q")
    print('{:5} {:5} {:5}'.format('p','q','p \u21d2 q'))

    p=True
    q=False

    for x in(p,q):
        for y in(p,q):
            print('{:<5} {:<5} {:<5}'.format(boolean_to_tf(x), boolean_to_tf(y), boolean_to_tf(iff(x, y))))