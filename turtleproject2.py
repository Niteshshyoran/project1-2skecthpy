
# from turtle import *
# color('blue',  'pink')
# speed(10)
# bgcolor("black")
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     backward(30)
#     forward(10)
#     left(38)
#     if abs(pos()) < 5:
#         break
# end_fill()
# hideturtle()
# done()









# #star
# from turtle import *
# color("black","silver")
# bgcolor("blue")
# speed(10)
# begin_fill()
# # for i in range(True):
# right(20)
# forward(100)
# # s.backward(50)
# for i in range(38):
#     right(199)
#     forward(199)
# end_fill()
# done()








#rainbow

from turtle import *
colors = ['purple', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
bgcolor('grey')
speed(20)
for x in range(270):
    pencolor(colors[x%7])
    width(x//100 + 1)
    forward(x)
    right(75)
hideturtle()
done()



# from turtle import *
# colors = ['blue', 'green', 'yellow',  'red', 'blue', 'green', 'yellow',  'red']
# bgcolor('black')
# speed(20)
# for x in range(270):
#     pencolor(colors[x%8])
#     width(x//100 + 1)
#     forward(x)
#     right(45)
# done()

