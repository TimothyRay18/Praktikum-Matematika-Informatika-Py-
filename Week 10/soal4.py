"""
Timothy
1119007
"""
def UbahBiner(n):
    n_reverse=n[::-1]
    posisi=0
    int_des=0
    for x in n_reverse:
        hasil_kali=int(x)*(2**posisi)
        int_des=int_des+hasil_kali
        posisi=posisi+1
    return int_des
if __name__ == "__main__":
    list_biner = ['0','1','10','11','100','101','110','111','1000']
    for x in list_biner:
        print('{:>4}'.format(x), end=' ')
        int_desimal = UbahBiner(x)
        print(int_desimal)