# 71200619-Untung Mangkunegara
# Materi 10 : Dictionary
# Referensi soal : UG 10 Grup C Nomor 4

# Anda akan diberikan list dengan elemen bertipe integer. Tugas anda adalah
# membuat fungsi yang akan mengelompokan setiap index dari elemen list tersebut ke
# dalam dictionary! Fungsi tersebut bernama kelompok_index(array) yang akan
# mengembalikan dalam bentuk dictionary.
# Input:
# test = ["a", "b", "h", "t", "b", "a", "n", "t", "b", "l"]
# print(kelompok_index(test))
# Output:
# {'a':[0,5], 'b':[1, 4, 8], dst }

# testcase
test=["a", "b", "h", "t", "b", "a", "n", "t", "b", "l"]

#Fungsi
def kelompok_index(array):
    kunci=list(dict.fromkeys(array))
    fix={}
    for i in kunci:
        stored=[]
        for a in range(len(array)):
            if array[a]==i:
                stored.append(a)
        fix[i]=stored
    print(fix)

kelompok_index(test)