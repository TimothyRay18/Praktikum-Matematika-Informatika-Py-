"""
1119007
Timothy Ray
"""

def buat_list_ekspresi_boolean(pengguna):
    list_pengguna=[]
    for x in pengguna:
        if(pengguna[x]==False):
            list_pengguna.append("not("+x+")")
        else:
            list_pengguna.append(x)
    return list_pengguna

if __name__ == "__main__":
    pengguna1= {'kopi':True,
                'susu':False,
                'teh':False}
    pengguna2= {'kopi':True,
                'susu':True,
                'teh':False}
    pengguna3= {'kopi':False,
                'susu':False,
                'teh':True}

    list_pilihan1=buat_list_ekspresi_boolean(pengguna1)
    print("pengguna1= ",end='')
    print(list_pilihan1)
    list_pilihan2=buat_list_ekspresi_boolean(pengguna2)
    print("pengguna2= ",end='')
    print(list_pilihan2)
    list_pilihan3=buat_list_ekspresi_boolean(pengguna3)
    print("pengguna3= ",end='')
    print(list_pilihan3)
    print()

    print("pengguna1= ",end='')
    str1=" and ".join(list_pilihan1)
    print(str1)
    list_pilihan2=buat_list_ekspresi_boolean(pengguna2)
    print("pengguna2= ",end='')
    str2=" and ".join(list_pilihan2)
    print(str2)
    list_pilihan3=buat_list_ekspresi_boolean(pengguna3)
    print("pengguna3= ",end='')
    str3=" and ".join(list_pilihan3)
    print(str3)
    print()

    list_semua=[]
    list_semua.append(str1)
    list_semua.append(str2)
    list_semua.append(str3)
    print("Semua pengguna")
    print(" or ".join(list_semua))
    print()