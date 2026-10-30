# def sumTo(n):
#     return (n * (n+1)) // 2
# # Test
# print(sumTo(10))  # Çıktı:55




# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
#
# print(sumTo(10))
#
# def mySqrt(n):
#     oldguess = n / 2.0
#     while True:
#         newguess = 0.5 * (oldguess + (n / oldguess))
#         if abs (newguess - oldguess) < 1e-10:
#             return newguess
#         oldguess = newguess
#
# print(mySqrt(25))
# print(mySqrt(2))


import turtle
#
# def drawSprite(t, num_legs, leg_length):
#     angle = 360 / num_legs
#     for _ in range(num_legs):
#         t.forward(leg_length)
#
#         for _ in range(3):
#             t.forward(10)
#             t.left(120)
#         t.backward(leg_length)
#         t.right(angle)
#
#
# def fancySquare(t, size):
#    for _ in range(4):
#     t.forward(size)
#     drawSprite(t, 8,20)
#     t.right(90)
#
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# fancySquare(t, 150)
# wn.mainloop()

# def check_number(number):
#      if number > 0:
#          return "positive"
#      elif number < 0:
#          return "negative"
#      else:
#          return "zero"
#
# print(check_number(5))
# print(check_number(-3))
# print(check_number(0))


# import turtle
# def drawBar(t, height, label_offset):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#
#
#     t.penup()
#     t.backward(20)
#     t.left(90)
#     t.forward(height + label_offset)
#
#     t.write(f"(height)", align="center", font=("Arial", 10, "normal"))
#
#     t.backward(height + label_offset)
#     t.right(90)
#     t.forward(20)
#     t.pendown
#
#
# def barChart(data):
#         screen = turtle.Screen()
#         screen.bgcolor("lightgreen")
#
#
#         t = turtle.Turtle()
#         t.color("blue", "tomato")
#         t.pensize(3)
#         t.speed(6)
#
#         max_val = max(data)
#         border = 40
#         screen.setworldcoordinates(-20, -20, len(data) * 45 + border, max_val + border + 20 )
#
#         label_offset = (max_val +  border) * 0.03
#
#
#         for val in data:
#             drawBar(t, val, label_offset)
#
#         t.hideturtle()
#         screen.mainloop()
#
#
# if __name__  == "__main__":
#     ornek_veri = [48, 117, 200, 240, 160, 260, 220]
#     barChart(ornek_veri)


