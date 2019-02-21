p = int(input("Masukan nilai N :  "))
import random
for x in range(p):
    x += 1
    a = random.uniform(0.0,0.5)
    print("Data ke : {} => {}".format(x,a))
print("Selesai")
