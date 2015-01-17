#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import Image as I

START = (0, 1)
END = (1022, 1021)
ROAD = (255, 255, 255)
WALL = (0, 0, 0)
WALK = (255, 0, 0)
STEP = ((1, 0), (-1, 0), (0, 1), (0, -1))

def main():
    img = I.open('maze.png')
    px, py = START
    ex, ey = END

    ans = []
    # 最初いんちき
    ans.append((px, py))
    prev = (px, py)
    px += 1

    nxt = []
    nr = 0
    while px != ex or py != ey:
        ans.append((px, py))
        t = []
        for sx, sy in STEP:
            n = (px + sx, py + sy)
            if n == prev:
                continue
            if img.getpixel(n) == WALL:
                continue
            t.append(n)
        if len(t) < 1:
            if len(nxt) < 1:
                print 'not clear!'
                return False
            p = nxt.pop()
            px = p[0][0]
            py = p[0][1]
            n = p[1]
            prev = p[2]
            ans = ans[:n]
        elif len(t) != 1:
            l = len(ans)
            prev = (px, py)
            for p in t[1:]:
                nxt.append((p, l, prev))
            px = t[0][0]
            py = t[0][1]
        else:
            prev = (px, py)
            px = t[0][0]
            py = t[0][1]
            nr += 1
            if nr >= 100:
                print '%4d, %4d, %d\r' % (px, py, len(ans)),
                nr = 0

    ans.append((ex, ey))
    for x, y in ans:
        img.putpixel((x, y), WALK)
    img.save('ans.png', 'PNG')

if __name__ == '__main__':
    main()
