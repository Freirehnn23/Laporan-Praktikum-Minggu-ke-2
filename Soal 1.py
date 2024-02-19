berat_badan = float(input('Masukan Nilai Berat Badan dalam (Kg): '))
tinggi_badan = float(input('Masukan Tinggi Badan dalam (M) : '))
bmi = berat_badan / (tinggi_badan**2)

print('BMI anda ialah %.1f' % (bmi))