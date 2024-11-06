import turtle
import random
# import colorgram


t = turtle.Turtle()
t.speed('fastest')
# t.pensize(1)
turtle.colormode(255)

# colors = colorgram.extract('image.jpg', 10)
# color_pallet = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     # rgb_tuple = tuple(color.rgb)
#     color_pallet.append(new_color)
# print(color_pallet)

# new_color_pallate = []
# for color in colors:
#     rgb_value = tuple(color.rgb)
#     new_color_pallate.append(rgb_value)
# print(new_color_pallate)

color_list =[(225, 233, 238), (236, 35, 109), (146, 26, 66),
             (10, 145, 91), (238, 73, 35), (223, 166, 47), (178, 159, 47)]

# colors = colorgram.extract("hirst.jpeg",10)
# for item in colors:
# color_list.append(tuple(item.rgb))

# print(color_list)
no_of_col = 10
no_of_rows = 10
initial_x = -225
initial_y = -225
t.penup()
t.hideturtle()
t.setpos(initial_x, initial_y)

for h in range(no_of_rows):
    for i in range(no_of_col):
        if i == no_of_col-1:
            t.dot(20,random.choice(color_list))
        else:
            t.dot(20,random.choice(color_list))
            t.fd(50)
    if h == no_of_rows-1:
        break
    else:
        t.setpos(initial_x,t.ycor()+50)

# t.screen.mainloop()
turtle.Screen()
turtle.exitonclick()