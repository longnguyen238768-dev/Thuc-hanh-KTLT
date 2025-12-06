print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


def benefit(t,n,k):
    if t<0 or n<=0 or k<=0:
        print('Không hợp lệ')
    else:
        A=n*((1 + t/100)**k)
        print(f'Số tiền nhận được sau {k} tháng là: {round(A,2)}')
t=float(input('Nhập lãi suất tiết kiệm(%/tháng): '))
n=float(input('Nhập số vốn ban đầu: '))
k=float(input('Nhập số tháng gửi: '))
benefit(t,n,k)
