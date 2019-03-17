"""
    绘制五角星
"""

import turtle


def main():
    size = 100
    for j in range(5):
        for i in range(5):
            turtle.forward(size)
            turtle.right(144)
        size = size + 35

    turtle.exitonclick()
    pass


if __name__ == '__main__':
    main()
