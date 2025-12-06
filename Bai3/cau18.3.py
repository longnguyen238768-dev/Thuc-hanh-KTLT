print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


n = int(input("Nhập n: "))

fib = [0, 1]
while fib[-1] + fib[-2] < n:
    fib.append(fib[-1] + fib[-2])

print("Các số Fibonacci nhỏ hơn n:")
print(fib)
