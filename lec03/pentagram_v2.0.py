"""
    绘制五角星
"""

import turtle


def draw_pentagram(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


def main():
    """
    主函数
    :return:
    """

    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 100
    for j in range(5):
        draw_pentagram(size)
        # size = size + 35
        size += 35

    turtle.exitonclick()


if __name__ == '__main__':
    main()
