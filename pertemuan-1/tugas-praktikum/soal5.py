a = int(input('Angka pertama: '))
b = int(input('Angka kedua: '))


def hitungJumlah(a, b):
    return (a+b)


def hitungKurang(a, b):
    return (a-b)


penjumlahan = hitungJumlah(a, b)
pengurangan = hitungKurang(a, b)

print(f'Hasil penjumlahan = {penjumlahan}')
print(f'Hasl pengurangan = {pengurangan}')
