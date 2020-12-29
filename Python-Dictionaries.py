#Dictionaries
#Dictionaries (Kamus) adalah suatu set dalam python, dictionaries terdiri dari :
# <Nama Kamus> = ('key' : 'value' , 'key' : 'value", .... 'key -n' : 'value -n')

#Membuat dictionary kamus1
kamus1={'barang1':80000, 'barang2':50000}

#print kamus1
kamus1 

#Data01
Data01={'Nama':'Paijo', 'umur':20}
Data01 

#Complex Dictionary
kompleks={'dd01':909,'dd02':[3,4,5],'dd3':{'KunciDalam':100}}
kompleks['dd02']

kompleks['dd02'][2]

kompleks['dd3']

kompleks['dd3']['KunciDalam']

#Complex 2
komplex={'kunci1':['r','s','t']}

komplex

#Modifikasi Dictionary

#Mengubah ke Kapital
komplex['kunci1'][2].upper()

#menambah kunci. Algoritma : []= *Cara ini juga bisa digunakan untuk merubah nilai kunci
komplex['kunci2']=100000000
komplex 

#mengambil nama kunci. Algoritma : .keys()
komplex.keys()

#mengambil isi nilai. Algoritma : .values()
komplex.values()

#pairing nilai
komplex.items()