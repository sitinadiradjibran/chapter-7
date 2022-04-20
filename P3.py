file = open("f:/data2.txt","r")
sum = 0
for data in file:
    try:  
       sum = sum + int(data)
    except: 
        print ("Karakter ini bukan merupakan sebuah angka > "+ data)
        
print("Jumlah = "+ str(sum))
