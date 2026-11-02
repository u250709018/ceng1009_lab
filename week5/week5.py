import random
#
# for i in range(10):
#     number = random.random()
#     print(number)


#
# import random
#
#
# for i in range(10):
#     number = random.randint(25,35)
#     print (number)


#
# import math
#
# a = float(input("Enter a number: "))
# b = float(input("Enter another number: "))
#
# c =math.hypot(a, b)
# print("The hypotenuse is:", c)


#
# import math
#
# def  areaOfCircle(r):
#     area = math.pi * r**2
#     return area
#
# result = areaOfCircle(5)
# print(result)
#
#
# import turtle
#
# def drawStar():
#     for i in range(5):
#         turtle.forward(100)
#         turtle.right(144)
#
# drawStar()
#
# turtle.done()



# import turtle
#
# def drawsquare():
#     for i in range(4):
#         turtle.forward(20)
#         turtle.left(90)
#
# turtle.penup()
# turtle.goto(-150,10)
# turtle.pendown()
#
# for i in range(5):
#     drawsquare()
#     turtle.penup()
#     turtle.forward(60)
#     turtle.pendown()
#
# turtle.done()


# import turtle
#
# turtle.bgcolor("lightgreen")
# turtle.pencolor("pink")
# turtle.pensize(4)
#
# def drawsquare():
#    for i in range(4):
#        turtle.forward(20)
#        turtle.left(90)
#
# turtle.penup()
# turtle.goto(-150,10)
# turtle.pendown()
#
# for i in range(5):
#     drawsquare()
#     turtle.penup()
#     turtle.forward(60)
#     turtle.pendown()
#
# turtle.done()

#
# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# alex = turtle.Turtle()
# alex.color("hotpink")
# alex.pensize(4)
#
#
# def drawsquare(t, size):
#   for i in range(4):
#         t.forward(size)
#         t.left(90)
#
# size = 20
#
#
# for i in range(5):
#         drawsquare(alex, size)
#         size = size + 20
#         alex.penup()
#         alex.forward(-10)
#         alex.right(90)
#         alex.forward(10)
#         alex.left(90)
#         alex.pendown()
#
#
# turtle.done()