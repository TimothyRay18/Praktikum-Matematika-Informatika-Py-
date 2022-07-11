""""
Timothy
1119007
"""

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

def PrintProduk(produk):
    if(len(produk)==0):
        print('-')
    else:
        str = (',').join(produk)
        print(str)

dict_pembeli_produk = {
    pembeli_1: {produk_2, produk_4, produk_8, produk_10},
    pembeli_2: {produk_1,produk_4,produk_5,produk_7},
    pembeli_3: set(),
    pembeli_4: {produk_3,produk_9},
    pembeli_5: {produk_2,produk_3,produk_4,produk_9},
    pembeli_6: {produk_2,produk_4,produk_5,produk_6,produk_10}
}

for x in dict_pembeli_produk:
    total = len(dict_pembeli_produk[x])
    print(x,end=' = ')
    print(total)
    PrintProduk(dict_pembeli_produk[x])