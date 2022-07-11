"""
1119007
Timothy Ray
"""
KALI = '\u00b7'
KOMPLEMEN = '\u2032'

def buat_list_ekspresi_boolean(pengguna):
    list_pengguna=[]
    for x in pengguna:
        for y in x:
            if(x[y]==0):
                list_pengguna.append(x+KOMPLEMEN)
            else:
                list_pengguna.append(x)
    return list_pengguna

if __name__ == "__main__":
    list_kombinasi=[
        {'k': 0,'s': 0,'t': 0,'x':0},
        {'k': 0,'s': 0,'t': 1,'x':1},
        {'k': 0,'s': 1,'t': 0,'x':1},
        {'k': 0,'s': 1,'t': 1,'x':1},
        {'k': 1,'s': 0,'t': 0,'x':1},
        {'k': 1,'s': 0,'t': 1,'x':0},
        {'k': 1,'s': 1,'t': 0,'x':1},
        {'k': 1,'s': 1,'t': 1,'x':0},
    ]

    print('{:2}{:2}{:2}{:2}'.format('k','s','t','x'))
    list_hasil=[]
    for a in list_kombinasi:
        print('{:<2}{:<2}{:<2}{:<2}'.format(a['k'],a['s'],a['t'],a['x']),end='')
        if(a['x']==1):
            list_baru=[]
            dict = a.copy()
            del(dict['x'])
            for x in dict:
                if dict[x]==1:
                    list_baru.append(x)
                else:
                    list_baru.append(x + "\u2032")
            print("".join(list_baru))
            list_hasil.append("".join(list_baru))
        else:
            print()
    print()
    print(" + ".join(list_hasil))