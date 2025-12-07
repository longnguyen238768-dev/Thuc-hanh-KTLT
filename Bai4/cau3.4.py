print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Ví dụ sử dụng
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
