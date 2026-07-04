import numpy as np
import matplotlib.pyplot as plt

def fibo(n):
    if n == 0:
        fibo_list = np.array([0])
    elif n == 1:
        fibo_list = np.array([0,1])
    else:
        f_0, f_1 = 0, 1
        fibo_list = np.array([f_0,f_1])
        for i in np.arange(n-2):
            fibo_num = f_0 + f_1
            fibo_list = np.append(fibo_list,fibo_num)
            f_0, f_1 = f_1, fibo_num
    return fibo_list

def find_o_xy(f_list):
    #起始圆心坐标
    x_n, y_n = 0, 0
    o_x_array, o_y_array = np.array([x_n]), np.array([y_n])
    for n in np.arange(1,len(f_list)):
        #需要注意pyhton中计数是从0开始
        #第一项作为起始点已经给出
        y_n=y_n+np.mod(n+1,2)*f_list[n]*(-1)**(1+(np.mod(n+1,2)+n+1)/2)
        x_n=x_n+np.mod(n,2)*f_list[n]*(-1)**(1+(np.mod(n+1,2)+n+1)/2)
        #横纵坐标(x,y)
        o_x_array = np.append(o_x_array, x_n)
        o_y_array = np.append(o_y_array, y_n)
    return o_x_array, o_y_array

def main():

    count = 100
    f_list = fibo(count)
    x0_array, y0_array = find_o_xy(f_list)

    # 各个正方形对应的边长,如例图半径从1,2...开始
    f_list_r = fibo(count + 2)[2::]

    # 画出各个正方形内的1/4圆
    start_angle, end_angle = np.pi, 1.5 * np.pi
    for n in np.arange(len(f_list)):
        t = np.arange(start_angle, end_angle, 0.001)
        circle_x = (f_list_r[n]) * (np.sin(t)) + x0_array[n]
        circle_y = (f_list_r[n]) * (np.cos(t)) + y0_array[n]

        start_angle += 0.5 * np.pi
        end_angle += 0.5 * np.pi

        plt.plot(circle_x, circle_y, color='b')

if __name__ == '__main__':
    main()
