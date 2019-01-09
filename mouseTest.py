#
# _*_ coding:UTF-8 _*_
from ctypes import *
import time
import datetime
import mouse as ms
import math as m

start_od = {'x': 100, 'y': 200}
end_od = {'x': 1500, 'y': 1000}
time_last = 5000
fps = 60


def distance(start, end):
    return m.sqrt(m.pow(end.x - start.x, 2) + m.pow(end.y - start.y, 2))


def drag(start, end, time_last, fps=60):
    ms.mouse_move(start['x'], start['y'])

    x_bias_pf = (end['x'] - start['x']) / time_last / 60 * 1000
    y_bias_pf = (end['y'] - start['y']) / time_last / 60 * 1000
    time_shift = 1000.0 / fps

    time_start = round(time.time() * 1000)
    time_cursor = round(time.time() * 1000)
    x = start['x']
    y = start['y']

    while round(time.time() * 1000) - time_start < time_last:
        if round(time.time() * 1000) - time_cursor > time_shift:
            time_cursor += time_shift
            x += x_bias_pf
            y += y_bias_pf
            ms.mouse_move(int(x), int(y))


if __name__ == "__main__":
    # ms.mouse_click(500, 280)
    # str1 = 'python'
    # ms.key_input(str1)
    # t1 = int(round(time.time() * 1000))
    # print(t1)
    #
    #
    # print(int(round(time.time() * 1000)))
    #
    # print(start_od)
    #
    #
    # print((end_od['x'] - start_od['x'])/time_last/60*1000)
    # print((end_od['y'] - start_od['y'])/time_last/60*1000)
    # # print((end_od.x - start_od.x)/time_last/60*1000)
    #
    # t2 = int(round(time.time() * 1000))
    # print(t2)
    #
    #
    #
    # print(t2-t1)

    # drag(start_od, end_od, time_last)

    ms.mouse_move(1000, 20)
    ms.mouse_down()
    drag({'x': 1000, 'y': 20},{'x': 1050, 'y': 200},100,120)
