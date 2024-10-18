#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'主程序 '

__author__ = 'haotian zhang'

import datetime
import time
import os
import csv
from generate_grid import generate_grid
from check_reward import check_reward
import config

#总奖励
sumrewards = 0
countnum = 100000 #执行次数
countwin = 0
winnumbers = []
freenumbers = []
buymoney = 0
freesum =0
countfree =0
betnum = 5 #下注等级，默认5

# 主程序
results = []
for i in range(countnum):
    grid,formatted_grid1 = generate_grid(betnum)
    #返回每行图标内容
    iconh1 = [grid[0][0],grid[0][1],grid[0][2],grid[0][3],grid[0][4]]
    iconh2 = [grid[1][0],grid[1][1],grid[1][2],grid[1][3],grid[1][4]]
    iconh3 = [grid[2][0],grid[2][1],grid[2][2],grid[2][3],grid[2][4]]

    #统计免费图标出现的次数
    freeicon = 0
    for row in grid:
        for element in row:
            if element == config.icons[0]:
                freeicon += 1
        
    #current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:")   #时间格式
    # 记录当前时间，以微秒为单位。用于精确的时间戳记录，例如在性能测试或时间戳记录中。
    current_time = int(round(time.time() * 1000000))  # 毫秒千分位
    # 将二维网格转换为一维字符串列表，方便后续处理或输出。每个子列表通过逗号加空格连接。
    formatted_grid = [", ".join(map(str, sublist)) for sublist in grid]  # 格子数据格式化    
    rewards = check_reward(grid)
    # 检查网格中的奖励，并返回总奖励值。此函数用于评估网格状态并计算相应的奖励。
    sumrewards += rewards
    # 累加获得的奖励，用于统计总奖励。
    
    # 将免费局数进行汇总
    match freeicon:
        case 3:
            freesum += 10
            countfree += 1
            freenumbers.append(freeicon)
            # 处理免费图标出现3次的情况。增加对应的奖励值，并记录出现次数。
        case 4:
            freesum += 10
            countfree += 1
            freenumbers.append(freeicon)
            # 处理免费图标出现4次的情况。增加对应的奖励值，并记录出现次数。
        case 5:
            freesum += 10
            countfree += 1
            freenumbers.append(freeicon)
            # 处理免费图标出现5次的情况。增加对应的奖励值，并记录出现次数。
        case _:
            freesum += 0
            # 默认情况，当免费图标出现次数不是3、4或5时，不增加奖励。

    # 结构化单轮游戏数据
    game_data = {
        "游戏编号": i + 1,
        "时间戳(千分毫秒)": current_time,
        "格子状态": formatted_grid,
        "奖励": rewards if rewards else "无",
        "1格子": ", ".join(iconh1),
        "2格子": ", ".join(iconh2),
        "3格子": ", ".join(iconh3),
        "免费图标个数":freeicon,
        "金发之前格子":formatted_grid1
        }
        
    # 将奖励计入总数和中奖次数
    if rewards:
        countwin += 1
        winnumbers.append(rewards)
        
    # 将结构化数据添加到结果列表
    results.append(game_data)

'''
    #输出中奖图标到文件
    current_time = int(round(time.time() * 1000000))  #毫秒千分位
    result_text = f"游戏 {i+1}: 时间：{current_time}"
    formatted_grid = [", ".join(map(str, sublist)) for sublist in grid]
    result_text += f"生成的格子： {', '.join(formatted_grid)} "  
    rewards = check_reward(grid)  
    sumrewards += rewards
    if rewards:
        result_text += f",获得奖励：{rewards} 分！\n"
        countwin += 1
        numbers.append(rewards)
    else:
        result_text += ",没有连续图标，无奖励。\n"  
    
    result_text += f"1格子： {', '.join(iconh1)}\n"  
    result_text += f"2格子： {', '.join(iconh2)}\n"  
    result_text += f"3格子： {', '.join(iconh3)}\n"  
    
    #result_text += "游戏结束\n"
    
    # 向结果列表中添加一个新的结果文本
    results.append(result_text)
'''

#统计每个奖励出现的次数
def count_occurrences(numbers):
    # 初始化一个空字典来存储每个数值及其出现的次数
    counts = {}
    
    # 遍历数值列表
    for number in numbers:
        # 如果数值已经在字典中，则增加其计数
        if number in counts:
            counts[number] += 1
        # 如果数值不在字典中，则添加到字典并设置计数为1
        else:
            counts[number] = 1
    
    return counts

# 向结果文本追加游戏统计信息
results1 =[]
# 记录游戏进行的总次数以及最终累计获得的奖励分数
result_text = f"游戏进行了{countnum}次，最终总奖励：{sumrewards} 分！\n"
# 计算并记录总中奖次数、中奖率（中奖次数除以游戏总次数）及平均每局获得的奖励
result_text += f"总中奖次数：{countwin} 次！中奖率为{countwin/countnum},平均每局奖励为{sumrewards/countnum}\n"
# 调用函数count_occurrences计算每个奖励出现的次数，并将结果附加到结果文本中
result_text += f"每个奖励出现的次数：{count_occurrences(winnumbers)} \n"
result_text += f"免费奖励出现的次数：{countfree} 局,累计获取免费次数：{freesum}！每个免费图标出现的次数{count_occurrences(freenumbers)}"

# 将这一轮的汇总结果添加到结果列表中
results1.append(result_text)

# 定义文件名，使用当前日期时间确保每次运行生成的文件名唯一
file_name = f"game_results_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# 获取当前工作目录
current_dir = os.getcwd() + '/temp'
# 构建文件路径
file_path = os.path.join(current_dir, file_name)

#file_path = os.path.join('/Users/xiaobai/Documents/pythontest/', file_name)

# 尝试以写入模式('w')打开文件，如果文件已存在则会被覆盖
try:
    with open(file_path, 'w', encoding='utf-8') as file:
        # 将结果列表中的所有字符串连接起来并一次性写入文件
        file.write(''.join(results1))
# 如果在文件操作过程中发生IO错误，则打印错误信息
except IOError as e:
    print(f"文件操作失败: {e}")

# 定义CSV文件的名称和路径
file_name = f"game_results_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
# 指定文件保存的路径
#csv_file_path = os.path.join('/Users/xiaobai/Documents/pythontest/', file_name)
csv_file_path = os.path.join(current_dir, file_name)

    # 将结构化数据写入CSV文件

    # 输出到csv文件
try:
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["游戏编号", "时间戳(千分毫秒)", "格子状态", "奖励", "1格子", "2格子", "3格子","免费图标个数","金发之前格子"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # 写入表头
        writer.writeheader()
            
            # 写入每轮游戏的详细数据
        for game in results:
            writer.writerow(game)
    print(f"汇总数据已成功写入到 {file_path}")            
    print(f"详细数据已成功写入到 {csv_file_path}")
except IOError as e:
    print(f"写入文件时发生错误: {e}")