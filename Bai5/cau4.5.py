print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")


# 1. Nhập thư viện Tkinter
from tkinter import *

# 2. Xây dựng cửa sổ đồ họa (a)
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200') # Kích thước cửa sổ (chiều rộng x chiều cao)

# Thêm một Label (đã có trong gợi ý, dùng để hiển thị kết quả)
lbl = Label(window, text="Hello Tkinter")
lbl.grid(column=0, row=0)

# 3. Xây dựng phương thức xử lý sự kiện phím bấm (c)
def clicked():
    # Phương thức này sẽ được gọi khi nút được bấm
    # Thay đổi nội dung của Label
    lbl.configure(text="Nút đã được bấm!", fg="blue")
    # Thay đổi tiêu đề của cửa sổ để minh họa thêm
    window.title("Sự kiện đã được xử lý")


# 4. Thêm một widget Button và thiết lập màu sắc (b & d)
# bg="green": Thiết lập màu nền của nút là xanh lá cây (background)
# fg="white": Thiết lập màu chữ của nút là trắng (foreground)
# command=clicked: Gán hàm 'clicked' để xử lý sự kiện khi nút được bấm
btn = Button(
    window,
    text="Bấm Tôi!",
    command=clicked,
    bg="green",  # Màu nền (background)
    fg="white"  # Màu chữ (foreground)
)
# Đặt nút ở cột 1, hàng 0
btn.grid(column=1, row=0, padx=10) # Thêm padx để có khoảng cách với Label

# 5. Vòng lặp chính để hiển thị cửa sổ
window.mainloop()
