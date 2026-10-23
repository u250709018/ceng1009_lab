# import turtle
# def drawPoly(someturtle, somesides, somesize):
#     angle = 360 / somesides
#
#     for i in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.right(angle)
#
#
# tess = turtle.Turtle()
# drawPoly(tess, 8, 50)
#
# turtle.done()


# import turtle
# def drawPoly(someturtle, somesides, somesize):
#     angle = 360 / somesides
#
#     for i in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.right(angle)
#
# tess = turtle.Turtle()
#
# for i in range(20):
#     drawPoly(tess, 4, 100)
#     tess.right(20)
#
# turtle.done()


# import turtle
# def drawSpiral(t, angle):
#     lenght = 1
#
#
#     for i in range(84):
#         t.forward(lenght)
#         t.right(angle)
#         lenght = lenght + 2
#
# tess = turtle.Turtle()
#
# tess.penup()
# tess.backward(110)
# tess.pendown()
#
# drawSpiral(tess, 89)
#
#
#
# turtle.done()
# import turtle
# def drawSpiral(t, angle):
#     lenght = 1
#
#     for i in range(84):
#         t.forward(lenght)
#         t.right(angle)
#         lenght = lenght + 2
#
# tess = turtle.Turtle()
#
#
# tess.home()
# tess.penup()
# tess.forward(90)
# tess.pendown()
#
#
# drawSpiral(tess, 89)
#
#
# turtle.done()

# import turtle
# def drawSpiral(t, angle):
#     lenght = 1
#
#     for i in range(84):
#         t.forward(lenght)
#         t.right(angle)
#         lenght = lenght + 2
#
# tess = turtle.Turtle()
#
#
# tess.home()
# tess.penup()
# tess.forward(90)
# tess.pendown()
#
#
# drawSpiral(tess, 90)
#
#
# turtle.done()

#
# import turtle
# def drawPoly(someturtle, somesides, somesize):
#     angle = 360 / somesides
#
#     for i in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.right(angle)
#
# def drawEquitriangle(someturtle, somesize):
#     drawPoly(someturtle, 3, somesize)
#
# tess = turtle.Turtle()
#
#
# drawEquitriangle(tess, 100)
#
# turtle.done()



# import turtle
# def drawPoly(someturtle, somesides, somesize):
#     angle = 360 / somesides
#
#     for i in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.right(angle)
#
#
# def drawStar(t):
#     for i in range(5):
#         t.forward(100)
#         t.right(144)
#
# tess = turtle.Turtle()
#
# screen = turtle.Screen()
# screen.bgcolor("light green")
#
# tess.penup()
# tess.backward(200)
# tess.pendown()
#
# for i in range(5):
#     drawStar(tess)
#
#
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()
#
#
# turtle.done()

#
# import turtle
# def drawSprite(t, numlegs, leglength):
#     angle = 360 / numlegs
#
#
#     for i in range(numlegs):
#         t.forward(leglength)
#         t.backward(leglength)
#         t.left(angle)
#
# tess = turtle.Turtle()
#
# drawSprite(tess, 15,120)
#
# turtle.done()
