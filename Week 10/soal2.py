"""
Timothy
1119007
"""
def UbahHexa(hexa):
    int_des=0
    posisi =0
    tuple_nilai=('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    hexa_reverse=hexa[::-1]
    for a in hexa_reverse:
        idx = tuple_nilai.index(a)
        hasil_kali = idx*(16**posisi)
        int_des=int_des+hasil_kali
        posisi=posisi+1
    return int_des;
if __name__ == "__main__":
    list_nilai_hexadecimal = ['E', 'F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B']
    for x in list_nilai_hexadecimal:
        print("0x",end='')
        print('{:2}'.format(x),end=' ')
        int_desimal=UbahHexa(x)
        print(int_desimal)