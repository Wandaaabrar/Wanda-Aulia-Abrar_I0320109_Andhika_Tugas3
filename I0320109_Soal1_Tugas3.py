#list teman wanda sebanyak 10
list =['eric', 'jeno', 'mark', 'kai', 'gama', 'lia', 'sea', 'munji', 'yena', 'repan']

#menampilkan list indeks no 4,6,7
print (list[4], list[6], list[7])

#mengganti nama teman pada list no 3,5,9
list [3] = 'arkan'
print ("nilai baru pada index 3 : ", list [3])
list [5] = 'esok'
print ("nilai baru pada index 5 : ", list [5])
list [9] = 'malam'
print ("nilai baru pada index 9 : ", list [9])

#menambahkan 2 nama teman
list.extend (["mendung","abrar"])
print (list)

#menampilkan semua teman wanda dengan perulangan
print ("teman wanda : ada {} orang".format (len (list)))
for teman in list :
    print (teman)

#menampilkan panjang list
print (len(list))
