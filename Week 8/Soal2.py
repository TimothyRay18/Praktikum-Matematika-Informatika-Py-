"""
Timothy
1119007
"""
KALI = '\u00b7'
KOMPLEMEN = '\u2032'
PI = '\u03A0'
SIGMA = '\u03A3'

if __name__ == "__main__":
    list_kombinasi = [
        {'k': 0, 's': 0, 't': 0, 'f': 0},
        {'k': 0, 's': 0, 't': 1, 'f': 1},
        {'k': 0, 's': 1, 't': 0, 'f': 1},
        {'k': 0, 's': 1, 't': 1, 'f': 0},
        {'k': 1, 's': 0, 't': 0, 'f': 1},
        {'k': 1, 's': 0, 't': 1, 'f': 0},
        {'k': 1, 's': 1, 't': 0, 'f': 1},
        {'k': 1, 's': 1, 't': 1, 'f': 0},
    ]
    list_kanonik=[]
    list_index = []
    print('{:2}{:2}{:2}{:2}{:9}{:9}'.format('','k','s','t','f(k,s,t)','minterm'))
    for x in range(8):
        print('{:<2}{:<2}{:<2}{:<2}{:<9}'.format(x,list_kombinasi[x]['k'],list_kombinasi[x]['s'],list_kombinasi[x]['t'],list_kombinasi[x]['f']),end='')
        list_hasil = []
        if(list_kombinasi[x]['f']==1):
            list_index.append(str(x))
            for y in list_kombinasi[x]:
                if(y!='f'):
                    if(list_kombinasi[x][y]==0):
                        list_hasil.append(y+KOMPLEMEN)
                    else:
                        list_hasil.append(y)
            str_hasil = "".join(list_hasil)
            list_kanonik.append(str_hasil)
        print("".join(list_hasil))
    print()

    print("Dalam bentuk kanonik SOP:")
    str_kanonik = " + ".join(list_kanonik)
    print("f(k,s,t) = "+str_kanonik)

    list_lambang = []
    for a in list_index:
        list_lambang.append('m'+a)
    print("Menggunakan lambang minterm: ")
    str_lambang = ' + '.join(list_lambang)
    print("f(k,s,t) = "+str_lambang)

    str_sigma = ','.join(list_index)
    print("Menggunakan lambang minterm dan sigma:")
    print("f(k,s,t) = "+SIGMA+'('+str_sigma+')')