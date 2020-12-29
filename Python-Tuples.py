#Tuple seperti list, tapi nilainya tidak dapat dirubah (Immutability)
#Contoh Tuple : (a,b,c) / (1,2,3)

t1=(7,8,9)
daftar=['jeruk','lemon']

#Melihat jenis data Algoritma : type()
type(t1)
type(daftar)


len(t1) #menghitung berapa elemen dalam tuple ini

t0=('x','a','b','x','x','e','a')
t0.count('x') #menghitung berapa banyak huruf 'x' diulang

t0.index('b') #melihat b ada di index berapa

#Contoh Immutability Tuple (Error terjadi)
t0[3]='AE'


