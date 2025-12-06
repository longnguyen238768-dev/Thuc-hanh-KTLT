print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


import math
def Tinh(R):
    if R<=0:
        print('R không hợp lệ (R phải >0)')
    else:
        chu_vi=2*math.pi*R
        dien_tich=math.pi*R*R
        print('Chu vi hình tròn:',round(chu_vi,2))
        print('Diện tích hình tròn:',round(dien_tich,2))
R=float(input('Nhập bán kính R: '))
Tinh(R)
