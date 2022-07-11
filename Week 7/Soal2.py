"""
1119007
Timothy Ray
"""
KALI = '\u00b7'
KOMPLEMEN = '\u2032'

def buat_list_ekspresi_boolean(pengguna):
    list_pengguna=[]
    for x in pengguna:
        if(pengguna[x]==0):
            list_pengguna.append(x+KOMPLEMEN)
        else:
            list_pengguna.append(x)
    return list_pengguna

if __name__ == "__main__":
    pengguna1= {'k':1,
                's':0,
                't':0}
    pengguna2= {'k':1,
                's':1,
                't':0}
    pengguna3= {'k':0,
                's':0,
                't':1}

    list_pilihan1=buat_list_ekspresi_boolean(pengguna1)
    print(list_pilihan1)
    list_pilihan2=buat_list_ekspresi_boolean(pengguna2)
    print(list_pilihan2)
    list_pilihan3=buat_list_ekspresi_boolean(pengguna3)
    print(list_pilihan3)
    print()

    str1=KALI.join(list_pilihan1)
    print(str1)
    list_pilihan2=buat_list_ekspresi_boolean(pengguna2)
    str2=KALI.join(list_pilihan2)
    print(str2)
    list_pilihan3=buat_list_ekspresi_boolean(pengguna3)
    str3=KALI.join(list_pilihan3)
    print(str3)
    print()

    list_semua=[]
    list_semua.append(str1)
    list_semua.append(str2)
    list_semua.append(str3)
    print(" + ".join(list_semua))
    print()