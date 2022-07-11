"""
Nama:Timothy
NIM:1119007
"""

if __name__ == "__main__":
    list_pq_values = [{'p': True, 'q': True},
                      {'p': True, 'q': False},
                      {'p': False, 'q': True},
                      {'p': False, 'q': False}]
    booleanFunc = input('Masukan ekspresi boolean: ')
    for x in list_pq_values:
        hasil=eval(booleanFunc, {'p':x['p'],'q':x['q']})
        x[booleanFunc]=hasil
    print(list_pq_values)