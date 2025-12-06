print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


a,b=1,2
total=0
print(a,end=" ")
while a <= 4000000:
    if a% 2==0:
        total +=a
    print (a,end=" ")
    a,b=b,a+b
print("Tong cac so chan trong day Fibonacci:", total)
