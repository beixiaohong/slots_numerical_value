#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'生成图标矩阵'

__author__ = 'haotian zhang'

import random
import config

def generate_grid(bet):
    """
    生成一个3行5列的图标网格，每个格子的图标根据其所在位置的权重分布随机选择。
    """
    grid = []
    for row_probs in config.grid_probs(bet):  # 遍历每行的权重分布
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
    return grid,formatted_grid1