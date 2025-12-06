print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


def get_sum(*num):
    tmp=0
#duyệt các tham số
    for i in num:
        tmp+=i
    return tmp
result=get_sum(1,2,3,4,5)
print(result)
