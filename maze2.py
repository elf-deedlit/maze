#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import Image as I

START = (0, 1)
END = (1022, 1021)
ROAD = (255, 255, 255)
WALL = (0, 0, 0)
STEP = ((1, 0), (-1, 0), (0, 1), (0, -1))

def count_wall(img, x, y):
    nvx = 0
    nvy = 0
    nr = 0
    for vx, vy in STEP:
        nx = x + vx
        ny = y + vy
        if img.getpixel((nx, ny)) == ROAD:
            nr += 1
            nvx = vx
            nvy = vy
    return (nr, nvx, nvy)

def main():
    img = I.open('maze.png')

    sx, sy = img.size
    # 行き止まりを埋める
    for y in xrange(1, sy - 1, 2):
        for x in xrange(1, sx - 1, 2):
            if img.getpixel((x, y)) != ROAD:
                continue
            nr, vx, vy = count_wall(img, x, y)
            if nr == 1:
                # 片っぽだけ壁なので行き止まりと見なす
                # 分かれ道まで全部埋める
                nx = x
                ny = y
                while nr == 1:
                    img.putpixel((nx, ny), WALL)
                    nx += vx
                    ny += vy
                    nr, vx, vy = count_wall(img, nx, ny)
    img.save('ans.png', 'PNG')

if __name__ == '__main__':
    main()
