# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     oneline
   Description :
   Author :       #TUYI#
   date：          29/9/2018
-------------------------------------------------
   Change Activity:
                   29/9/2018:
-------------------------------------------------
"""
__author__ = '#TUYI#'

map(lambda x: x**2, range(10))

# 一行输出心
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30,30)]) for y in range(30, -30, -1)]))

# 一行代码输出斐波那契数列

print([x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0]+a[i][1]])) for a in([[1, 1]], ) for i in range(30)]])



