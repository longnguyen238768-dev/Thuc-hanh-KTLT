print(" Sinh vien : Nguyen Duc Long")
print(" Ma so SV: 245751030110072")
print("##############################")

import turtle

# Tạo bút vẽ
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)      
turtle.bgcolor("white")

colors = ["red", "green", "blue"]

# Vẽ 12 vòng tròn xoay đều 30 độ
for i in range(12):
    painter.pencolor(colors[i % 3])   
    painter.circle(100)
    painter.left(30)                  

turtle.done()
