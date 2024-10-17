#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'生成图标矩阵'

__author__ = 'haotian zhang'

import random
import config

def generate_grid():
    """
    生成一个3行5列的图标网格，每个格子的图标根据其所在位置的权重分布随机选择。
    """
    grid = []
    for row_probs in config.grid_probs:  # 遍历每行的权重分布
        row = []
        for col_prob in row_probs:  # 遍历每格的权重
            # 确保权重列表与图标数量匹配
            if len(col_prob) != len(config.icons):
                raise ValueError("The length of weight distribution does not match the number of icons.")
            # 根据权重选择图标
            icon = random.choices(config.icons, weights=col_prob, k=1)[0]  # 修正了权重应用
            row.append(icon)
        grid.append(row)
        
    formatted_grid1 = [", ".join(map(str, sublist)) for sublist in grid]    

    #统计金发个数
    wild1num = 0
    for row in grid:
        for element in row:
            if element == config.icons[0]:
                wild1num += 1

    #金发个数达到2个，找出金发列下标
    b = []  # 存放列下标
    if wild1num >= 2:
        for i, row in enumerate(grid):
            for j,value in enumerate(row):
                if value == config.icons[0]:
                    b.append(j)  # 添加列下标到b数组

    #将金发所在列全部更新为金发，3为3行都需要修改
    for i in range(3):
        for j in b:
            grid[i][j] = config.icons[0]

    return grid,formatted_grid1