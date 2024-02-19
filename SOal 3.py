Gaji_perjam = int(input('Masukan Gaji Yang Anda Inginkan: '))
jamkerja_perminggu = int(input('Masukan Jam Kerja Anda Selama Satu Minggu: '))

pendapatan_kotor = Gaji_perjam * (jamkerja_perminggu * 5) 
pembayaran_pajak = pendapatan_kotor - (pendapatan_kotor * (14/100))
membeli_pakaian_aksesoris = pembayaran_pajak - (pembayaran_pajak * (10/100))
membeli_alat_tulis = pendapatan_kotor -(pendapatan_kotor * (1/100))
sedekah = pendapatan_kotor -(pendapatan_kotor * (25/100))
anak_yatim = (sedekah // 1000) * (30/100)
kaum_duafa = sedekah - anak_yatim

print('Total Gaji Budi Sebelum Membayar Pajak: Rp. ' , pendapatan_kotor)
print('Total Gaji Budi Setelah Mmebayar Pajak: Rp. ' , pembayaran_pajak)
print('Jumlah Uang Budi Untuk Membeli Pakaian dan Aksesoris: Rp. ' , membeli_pakaian_aksesoris)
print('Jumlah Uang Budi Untuk Membeli Alat Tulis: Rp. ' , membeli_alat_tulis)
print('Jumlah Uang Budi yang Di Sedekahkan: Rp. ' , sedekah)
print('Jumlah yang Diterima Anak Yatim : Rp. ' , anak_yatim)
print('Jumlah yang Diterima Kaum Duafa: Rp. ' , kaum_duafa)

