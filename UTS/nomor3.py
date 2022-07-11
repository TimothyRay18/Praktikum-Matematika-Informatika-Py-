"""
Nama:Timothy
NIM:1119007
"""
def implies(p,q):
    return not p or q
if __name__ == "__main__":
    list_pq_values = [
        {'p' : True, 'q' : True},
        {'p' : True, 'q' : False},
        {'p' : False, 'q' : True},
        {'p' : False, 'q' : False},
    ]
    print('{:6}{:6}{:6}'.format('p','q','p->q'))
    for x in list_pq_values:
        print('{:6}{:6}{:6}'.format(str(x['p']),str(x['q']),str(implies(x['p'],x['q']))))