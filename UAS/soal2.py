"""
Timothy
1119007
"""

def tambah_pembeli(dict,nama):
    cekDict = False
    for x in dict:
        if(x==nama):
            cekDict=True
    if(cekDict==False):
        dict[nama]=set()

def tambah_produk_pembeli(dict,nama,barang):
    dict[nama].add(barang)

def PrintProduk(produk):
    if(len(produk)==0):
        print('-')
    else:
        str = (',').join(produk)
        print(str)

if __name__ == "__main__":
    pembeli_1 = 'Timothy'
    pembeli_2 = 'Levin'
    pembeli_3 = 'Andre'
    pembeli_4 = 'Aristo'
    pembeli_5 = 'Fedly'
    pembeli_6 = 'Jeddi'
    produk_1 = 'Shampoo'
    produk_2 = 'Sabun'
    produk_3 = 'Air mineral'
    produk_4 = 'Snack'
    produk_5 = 'Panadol'
    produk_6 = 'Krupuk'
    produk_7 = 'Minuman'
    produk_8 = 'Tissue'
    produk_9 = 'Buku'
    produk_10 = 'Obat nyamuk'

    dict_pembeli_produk = {}

    tambah_pembeli(dict_pembeli_produk,pembeli_1)
    tambah_pembeli(dict_pembeli_produk,pembeli_2)
    tambah_pembeli(dict_pembeli_produk,pembeli_3)
    tambah_pembeli(dict_pembeli_produk,pembeli_4)
    tambah_pembeli(dict_pembeli_produk,pembeli_5)
    tambah_pembeli(dict_pembeli_produk,pembeli_6)

    tambah_produk_pembeli(dict_pembeli_produk,pembeli_1,produk_2)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_1,produk_4)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_1,produk_8)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_1,produk_10)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_2,produk_1)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_2,produk_4)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_2,produk_5)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_2,produk_7)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_4,produk_3)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_4,produk_9)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_5,produk_2)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_5,produk_3)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_5,produk_4)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_5,produk_9)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_6,produk_2)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_6,produk_4)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_6,produk_5)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_6,produk_6)
    tambah_produk_pembeli(dict_pembeli_produk,pembeli_6,produk_10)

    for x in dict_pembeli_produk:
        total = len(dict_pembeli_produk[x])
        print(x, end=' = ')
        print(total)
        PrintProduk(dict_pembeli_produk[x])