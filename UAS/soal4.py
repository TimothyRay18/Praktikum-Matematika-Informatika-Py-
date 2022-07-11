"""
Timothy
1119007
"""

def PrintProduk(produk):
    if(len(produk)==0):
        print('-')
    else:
        str = (',').join(produk)
        print(str)

def koefisien_kemiripan_dice(set1,set2):
    kardinalitas1=len(set1)
    kardinalitas2=len(set2)
    irisan = set1 & set2
    kardinalitas_set_irisan=len(irisan)
    kemiripan=2*kardinalitas_set_irisan/(kardinalitas1+kardinalitas2)
    return kemiripan

def rekomendasi_produk(set1,set2):
    selisih = set2-set1
    if(len(selisih)==0):
        return '-'
    else:
        return selisih

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

    dict_pembeli_produk = {
        pembeli_1: {produk_2, produk_4, produk_8, produk_10},
        pembeli_2: {produk_1, produk_4, produk_5, produk_7},
        pembeli_3: set(),
        pembeli_4: {produk_3, produk_9},
        pembeli_5: {produk_2, produk_3, produk_4, produk_9},
        pembeli_6: {produk_2, produk_4, produk_5, produk_6, produk_10}
    }

    nama = input("Masukan nama: ")
    print("Pembeli: "+nama)
    print("Nilai kemiripan dengan pembeli lain: ")
    for x in dict_pembeli_produk:
        if(x!=nama):
            kemiripan = koefisien_kemiripan_dice(dict_pembeli_produk[nama],dict_pembeli_produk[x])
            rekomen = rekomendasi_produk(dict_pembeli_produk[nama],dict_pembeli_produk[x])
            print(x,end=' = ')
            print(kemiripan,end=' : ')
            print(rekomen)