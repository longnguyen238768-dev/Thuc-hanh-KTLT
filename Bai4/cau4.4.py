print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


class py_solution:
    def roman_to_int(self, s):
        # Bảng giá trị La Mã
        rom_val = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        int_val = 0

        # Duyệt từng ký tự
        for i in range(len(s)):
            # Nếu ký tự đứng trước nhỏ hơn ký tự đứng sau → trừ
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]

        return int_val


# Ví dụ sử dụng
print(py_solution().roman_to_int("MCMIV"))     # 1904
print(py_solution().roman_to_int("MMMDCCCLXXX")) # 3880
print(py_solution().roman_to_int("C"))         # 100
