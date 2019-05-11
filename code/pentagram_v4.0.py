# Author: Ronnie Lee
# mail:ronnie14165@gmail.com
# url:ronnie14165.github.com
import turtle
# turtle.forward(distance)
# turtle.backward(distance)
# turtle.right(degree)      turn right
# turtle.left(degree)       turn left
# turtle.penup()
# turtle.pendown()
# turtle.pencolor()
# turtle.pensize()
# turtle.speed()
# turtle.exitonclick()      hold on

# fractal_tree.py
# 递归（迭代）函数：在函数中调用自身
# 分形树：具有相似性的几何图形


def draw_branch(branch_length):
    if branch_length > 0:
        turtle.forward(branch_length)
        print('Go forward', branch_length)
        turtle.right(20)
        print('Turn right 20 degree')
        draw_branch(branch_length - 15)

        turtle.left(40)
        print('Turn left 40 degree')
        draw_branch(branch_length - 15)

        turtle.right(20)
        print('Turn right 20 degree')
        turtle.backward(branch_length)
        print('Go backward', branch_length)


def main():
    turtle.pensize(2)
    turtle.pencolor('red')
    turtle.speed(3)
    turtle.right(270)

    turtle.penup()
    turtle.backward(150)
    turtle.pendown()

    draw_branch(60)

    turtle.exitonclick()


if __name__ == main():
    main()

