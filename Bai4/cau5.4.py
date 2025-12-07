print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

# Ví dụ sử dụng
print(py_solution().reverse_words('hello .py'))
