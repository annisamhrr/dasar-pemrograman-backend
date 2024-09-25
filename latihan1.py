#contoh1 tanpa menggunakan titik koma
print("Apa Kabar")
web="SIKOM Banyuwangi"
print("Sedang belajar bahasa Phyton di "+web)
print("Semangat!!")

#contoh2 menggunakan titik koma
print("Apa Kabar");
web="SIKOM Banyuwangi";
print("Sedang belajar bahasa Phyton di "+web);
print("Semangat!!");

#contoh3 menggunakan titik koma dan digabung menjadi satu baris
print("Apa Kabar");web="SIKOM Banyuwangi";print("Sedang belajar bahasa Phyton di "+web);print("Semangat!!")

#contoh comments
print("Apa Kabar");
web="STIKOM Banyuwangi"; 
Web="STIKOM PGRI"
WEB="STIKOM PGRI Banyuwangi Kota"
print("Sedang belajar bahasa Phyton di "+web)
print("Sedang belajar bahasa Phyton di "+Web)
print("Sedang belajar bahasa Phyton di "+WEB)
print("Semangat!!")

#variabel
website = "STIKOM Banyuwangi"
print(website)
harga = 5500
print(harga)
sukses = True
print(sukses)

#Type Data
#Tipe Data String
web = "Belajar Phyton di STIKOM Banyuwangi"
print(web)
#Tipe Data Integer
web = 1500
print(web)
#Tipe Data Float
web = 99.123
print(web)
#Tipe Data Complex Number
web = 4j
print(web)
#Tipe Data Boolean
web = True
print(web)
#Tipe Data List
web = ["satu","dua","tiga","satu"]
#Tipe Data Tuple
web = ("satu","dua","tiga","empat")
#Tipe Data Dictionary
web = {"satu":1,"dua":2.13,"tiga":"a", "empat": True}
print(web)

#operator aritmatika
x = 20
y = 6

print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x % y =',x%y)
print('x ** y =',x**y)

#operator perbandingan/relational
x = 7
y = 10

print('x =',x)
print('y =',y)
print('\n')

print('x == y hasilnya',x==y)
print('x != y hasilnya',x!=y)
print('x > y hasilnya',x>y)
print('x < y hasilnya',x<y)
print('x >= y hasilnya',x>=y)
print('x <= y hasilnya',x<=y)

#operator logika
print('Hasil dari True and True    :', True and True)
print('Hasil dari True and False   :', True and False)
print('Hasil dari False and True   :', False and True)
print('Hasil dari False and False  :', False and False)

print('\n')

print('Hasil dari True or True    :', True or True)
print('Hasil dari True or False   :', True or False)
print('Hasil dari False or True   :', False or True)
print('Hasil dari False or False  :', False or False)

print('\n')

print('Hasil dari not True  :', not True)
print('Hasil dari not False :', not False)

#operator bitwise
x = 10
y = 12

print('x berisi angka',x ,'desimal atau',bin(x),'biner')
print('y berisi angka',y ,'desimal atau',bin(y),'biner')

print('\n')

print('x & y   :',x & y)
print('x | y   :',x | y)
print('x ^ y   :',x ^ y)
print('~x      :',~x)
print('x << 1  :',x << 1)
print('x >> 1  :',x >> 1)

#operator assigment
a = 5
b = 3
b = b + 1
c = a + b
d = c + c + a
e = (c + d)* a

print('Isi variabel a:',a)
print('Isi variabel b:',b)
print('Isi variabel c:',c)
print('Isi variabel d:',d)
print('Isi variabel e:',e)

#Operator Identitas
a = 5
b = 5 
c = 6
print('a is b :', a is b)
print('a is c :', a is c)
print('a is not c :', a is not c)
print('\n')

i = 'STIKOM'
j = 'STIKOM'
print('i is j :', i is j)
print('i is not j :', i is not j)
print('\n');

x = ['a','b','c']
y = ['a','b','c']
print('x is y :', x is y)
print('x is not y :', x is not y)

#Operator Keanggotaan
bar = ['a','b','c']
print('bar :',bar)
print('\'a\' in bar        :', 'a' in bar)
print('\'a\' not in bar    :', 'a' not in bar)
print('\'d\' not in bar    :', 'd' not in bar)
print('\n')

baz = (12,43,102,55)
print('baz :',baz)
print('102 in baz      :', 102 in baz)
print('102 not in baz  :', 102 not in baz)
print('35 not in baz   :', 35 not in baz)

#Kondisi if bahasa phyton
#contoh1
a = 12
b = 10

if a > b:
    print('Variasi a lebih besar dari variasi b')

#contoh2
a = 12
b = 12

if a > b:
    print('Variabel a lebih besar dari variabel b')
if a < b:
    print('Variabel a lebih kecil dari variabel b')
if a ==b:
    print('Variabel a sama dengan variabel b')

#contoh3
a = 7

if (a % 2) == 0:
    print('variabel a berisi angka genap')
if (a % 2) !=0:
    print('Variabel a berisi angka ganjil')

#contoh
nilai = 65

if nilai >= 75:
    print('Selamat, anda lulus')
else:
    print('maaf, silahkan coba lagi tahun depan')

#Kondisi perulangan While
#contoh1
i = 1
while i <= 5:
    print('STIKOM')

#contoh2
i = 1
while i <= 5:
    print('STIKOM')
    i += 1

#contoh3
i = 1
while i <= 5:
    print('STIKOM', i)
    i += 1

#contoh4
i = 3
while i < 100:
    print('STIKOM', i)
    i = i + 3

#Kondisi perulangan For
warna =['Merah','Biru','Kuning','Biru']
for i in warna:
    print(i)

#Penggunaan function range()
#contoh1
for i in range(5):
    print(i)

#contoh2
for i in range(5,10):
    print(i)

#contoh3
for i in range(3,100,3):
    print(i)

#Perintah break bahasa phyton
#contoh1
i = 1
while i <= 10:
    print(i,' x ',i ,' = ',i*i)
    i +=1

#contoh2
i = 1
while i <= 10:
    print(i,' x ',i ,' = ',i*i)
    if i == 5:
        break
    i += 1

#Perintah continue dalam phyton
#contoh1
for i in range(1,11):
    print(i,' x ',i ,' = ',i*i)

#contoh2
for i in range(1,11):
    if 1 == 5:
        continue
    print(i,' x ',i ,' = ',i*i)

#contoh3
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i,' x ',i ,' = ',i*i)