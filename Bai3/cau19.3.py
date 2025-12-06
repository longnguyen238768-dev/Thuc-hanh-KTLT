print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


limit = 1_000_000
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if prime[i]:
        for j in range(i*i, limit + 1, i):
            prime[j] = False

P = tuple(i for i in range(limit + 1) if prime[i])
print("Tuple P đã tạo xong, số lượng số nguyên tố:", len(P))
