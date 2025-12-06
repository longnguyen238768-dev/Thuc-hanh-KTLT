print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


s = input("Nhập chuỗi: ")

new_s = ""
for ch in s:
    if not ch.isdigit():
        new_s += ch

print("Chuỗi sau khi bỏ chữ số:", new_s)
