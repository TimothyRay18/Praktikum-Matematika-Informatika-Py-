"""
Timothy
1119007
"""

if __name__ == "__main__":
    graf = {
        'Paulo': ['Max', 'Igor', 'Andreas', 'Derrick', 'Eloy'],
        'Max': ['Paulo', 'Igor'],
        'Igor': ['Max', 'Paulo', 'Andreas'],
        'Andreas': ['Igor', 'Derrick', 'Paulo'],
        'Derrick': ['Andreas', 'Paulo'],
        'Eloy': ['Paulo', 'Bella'],
        'Bella': ['Eloy'],
        'Gloria': ['Roxanne'],
        'Roxanne': ['Gloria']
    }

    #A
    nama = input("Masukan nama: ")

    #B
    list_simpul_terhubung=[]
    list_simpul_terlihat = []
    list_simpul_terlihat.append(nama)

    print("simpul dicapai: ",end='')
    print(list_simpul_terhubung)
    print("simpul dikenali: ",end='')
    print(list_simpul_terlihat)
    print()

    while(len(list_simpul_terlihat)!=0):
        simpul_diproses=list_simpul_terlihat.pop(0)
        print("diproses: "+simpul_diproses)
        print("simpul dikenali: ",end='')
        print(list_simpul_terlihat)
        list_tetangga=graf[simpul_diproses]
        for x in list_tetangga:
            if x not in list_simpul_terhubung:
                if x not in list_simpul_terlihat:
                    list_simpul_terlihat.append(x)
        list_simpul_terhubung.append(simpul_diproses)
        print("simpul dicapai: ",end='')
        print(list_simpul_terhubung)
        print("tetangga "+simpul_diproses+": ",end='')
        print(list_tetangga)
        print("simpul dikenali(sesudah): ",end='')
        print(list_simpul_terlihat)
        print()

    print("simpul yang dicapai "+nama+": ")
    print(list_simpul_terhubung)