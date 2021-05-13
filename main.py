# using colorgram to extract the colors from the image
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# importing pre-installed python library turtle
import turtle
import random

# changing the color mode to RGB
turtle.colormode(255)

# creating a brush object from the turtle class
brush = turtle.Turtle()

# creating a color list as extracted from a template image
color_list = [(241, 222, 85), (34, 98, 186), (85, 174, 219), (169, 67, 36), (217, 158, 84), (188, 15, 34), (174, 49, 86), (76, 107, 213), (227, 56, 101), (163, 163, 21), (168, 26, 16), (234, 68, 43), (73, 176, 77), (226, 122, 173), (124, 198, 117), (21, 54, 147), (58, 119, 63), (117, 226, 183), (71, 30, 43), (134, 216, 233), (239, 157, 218), (40, 173, 186), (29, 41, 85), (243, 174, 151), (162, 164, 237), (90, 31, 22)]

# setting brush speed
brush.speed("fastest")

# using penup() so the lines do not show
brush.penup()

# hiding the brush head
brush.hideturtle()

# fixing the position of the brush
brush.setheading(225)
brush.forward(325)
brush.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    # choosing a random color
    brush.dot(25, random.choice(color_list))

    # moving the brush up
    brush.forward(50)
    if dot_count % 10 == 0:
        brush.setheading(90)
        brush.forward(50)
        brush.setheading(180)
        brush.forward(500)
        brush.setheading(0)

# creating a screen object from the turtle module
screen = turtle.Screen()

# screen will exit once it is clicked
screen.exitonclick()