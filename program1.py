a=100000000
for x in range(1,9):
    if(x>=1 and x<=2):
       b=a*0
       print("Laba bulan ke- {} sebesar : {}".format(x,b))
    if(x>=3 and x<=4):
       c=a*0.1
       print("Laba bulan ke- {} sebesar : {}".format(x,c))
    if(x>=5 and x<=7):
       d=a*0.5
       print("Laba bulan ke- {} sebesar : {}".format(x,d))
    if(x==8):
       e=a*0.2
       print("Laba bulan ke- {} sebesar : {}".format(x,e))
jumlah=b+b+c+c+d+d+d+e
print("Total laba adalah : ",jumlah)



       #bulan= 8
#laba = [0,0,1000000,1000000,5000000,5000000,5000000,2000000]
#for i in laba:
   
#    print("Laba bulan ke- {} sebesar : {}".format(i,laba))
#   x = int(input("Laba bulan ke- {} sebesar : ".format(i)))
#    laba.append(x)
#print("Total laba adalah : ",sum(laba))
               
