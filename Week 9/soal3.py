"""
Timothy
1119007
"""
def hitung_kemiripan_by_jaccard(a,b):
    setA = a & b
    setB = a | b
    A = len(setA)
    B = len(setB)
    if(A>B):
        return B/A
    else:
        return A/B

def hitung_selisih(a,b):
    hasil=a-b
    return hasil

if __name__ == "__main__":
    transaksi_jordie = ["Dragon Hoops", "Dragon Hoops", "Booked", "The Crossover", "Rebound"]
    transaksi_sarah = ["The Oracle Code", "Under The Moon", "Overdrive", "The Crossover"]
    transaksi_shannon = ["Breaking Glass", "Breaking Glass"]
    transaksi_steve = ["Breaking Glass", "Dragon Hoops", "The Crossover","Nightwalker"]
    transaksi_manuel = ["Booked","Overdrive","Dragon Hoops","The Crossover","The Playbook"]

    set_jordie = set(transaksi_jordie)
    set_sarah = set(transaksi_sarah)
    set_shannon = set(transaksi_shannon)
    set_steve = set(transaksi_steve)
    set_manuel = set(transaksi_manuel)

    produk_fav = {
        "Jordie": set_jordie,
        "Sarah": set_sarah,
        "Shannon": set_shannon,
        "Steve": set_steve,
        "Manuel": set_manuel
    }

    for x in produk_fav:
        print(x,end=' ')
        print(produk_fav[x])
    print()

    nama1 = input("Masukkan nama pelanggan yang sedang belanja: ")

    for x in produk_fav:
        if(x!=nama1):
            hasil = hitung_kemiripan_by_jaccard(produk_fav[nama1],produk_fav[x])
            print("Nilai kemiripan dengan "+x+" = ",end='')
            print(hasil)
    print()

    nama2 = input("Berdasarkan nilai tertinggi (paling mirip), masukkan nama pelanggan untuk dasar rekomendasi: ")
    print("Berdasarkan daftar pembelian "+nama1+", rekomendasi pembelian untuk "+nama1+" adalah: ")
    hasil = hitung_selisih(produk_fav[nama2],produk_fav[nama1])
    print(hasil)