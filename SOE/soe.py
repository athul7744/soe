import time
start_time = time.time()
a=[]
b=[]
j=0

l=int(input("Enter the size : "))
for i in range(2,l):
    a.append(i);
    b.append(0);

for i in range(0,l-2):
    j=i
    while(j<l-2):
        j=j+a[i]
        try:
            if b[j] != 1 :
                b[j]=1
        except IndexError:
            break

for i in range(0,l-2):
    if b[i]==0:
        print(a[i])
print("\n--- %s seconds ---" % (time.time() - start_time))
