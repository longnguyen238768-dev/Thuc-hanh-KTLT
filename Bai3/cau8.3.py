print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


words = input("Nhập các từ: ").split()

max_len = max(len(w) for w in words)

print("Các từ dài nhất:")
for w in words:
    if len(w) == max_len:
        print(w)
