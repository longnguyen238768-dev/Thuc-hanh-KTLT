print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


ds=input('Nhap chuoi: ').split()
if len(ds) >= 2:
    new_ds = ds[1:-1]
else:
    new_ds = []

print("List sau khi bỏ phần tử đầu và cuối:", new_ds)
