print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r


# Ví dụ sử dụng
c = Circle(5)
print("Diện tích:", c.area())
print("Chu vi:", c.perimeter())
