#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'计算奖励分数 '

__author__ = 'haotian zhang'

import config

# 检查游戏网格中的图标组合，计算奖励分数
# 检查连续图标并给予奖励
def check_reward(grid):
    # 初始化奖励分数
    rewards = 0

    # 定义每个图标在不同连击数下的奖励分数
    icon_groups = config.icon_weights

    # 存储每列图标列表
    iconlist1 = [grid[0][0],grid[1][0],grid[2][0]]
    iconlist2 = [grid[0][1],grid[1][1],grid[2][1]]
    iconlist3 = [grid[0][2],grid[1][2],grid[2][2]]
    iconlist4 = [grid[0][3],grid[1][3],grid[2][3]]
    iconlist5 = [grid[0][4],grid[1][4],grid[2][4]]    
    
    # 初始化当前连击数
    current_streak = 1 
    
    # 根据第一行图标在其他行中的出现情况，确定当前的连击数
    #第一个图标是否中奖，
    if iconlist1[0] not in iconlist2 and not any(icon in iconlist2 for icon in (config.icons[1], config.icons[0])):
        current_streak = 1
    elif iconlist1[0] not in iconlist3 and not any(icon in iconlist3 for icon in (config.icons[1], config.icons[0])):
        current_streak = 2
    elif iconlist1[0] not in iconlist4 and not any(icon in iconlist4 for icon in (config.icons[1], config.icons[0])):
        current_streak =3
    elif iconlist1[0] not in iconlist5 and not any(icon in iconlist5 for icon in (config.icons[1], config.icons[0])):
        current_streak =4
    else:
        current_streak=5      
    
    # 计算当前图标在每一行中的数量
    iconnum2 = iconlist2.count(iconlist1[0])+iconlist2.count(config.icons[0])+iconlist2.count(config.icons[1])
    iconnum3 = iconlist3.count(iconlist1[0])+iconlist3.count(config.icons[0])+iconlist3.count(config.icons[1])
    iconnum4 = iconlist4.count(iconlist1[0])+iconlist4.count(config.icons[0])+iconlist4.count(config.icons[1])
    iconnum5 = iconlist5.count(iconlist1[0])+iconlist5.count(config.icons[0])+iconlist5.count(config.icons[1])

    # 根据当前连击数和图标数量，计算奖励分数
    match current_streak:
        case 1:
            rewards1 = icon_groups[iconlist1[0]][current_streak]
        case 2:
            rewards1 = icon_groups[iconlist1[0]][current_streak]*iconnum2
        case 3:
            rewards1 = icon_groups[iconlist1[0]][current_streak]*iconnum2*iconnum3
        case 4:
            rewards1 = icon_groups[iconlist1[0]][current_streak]*iconnum2*iconnum3*iconnum4
        case _:
            rewards1 = icon_groups[iconlist1[0]][current_streak]*iconnum2*iconnum3*iconnum4*iconnum5

    #第二个图标是否中奖
    if iconlist1[1] not in iconlist2 and not any(icon in iconlist2 for icon in (config.icons[1], config.icons[0])):
        current_streak = 1
    elif iconlist1[1] not in iconlist3 and not any(icon in iconlist3 for icon in (config.icons[1], config.icons[0])):
        current_streak = 2
    elif iconlist1[1] not in iconlist4 and not any(icon in iconlist4 for icon in (config.icons[1], config.icons[0])):
        current_streak =3
    elif iconlist1[1] not in iconlist5 and not any(icon in iconlist5 for icon in (config.icons[1], config.icons[0])):
        current_streak =4
    else:
        current_streak=5   

    iconnum2 = iconlist2.count(iconlist1[1])+iconlist2.count(config.icons[0])+iconlist2.count(config.icons[1])
    iconnum3 = iconlist3.count(iconlist1[1])+iconlist3.count(config.icons[0])+iconlist3.count(config.icons[1])
    iconnum4 = iconlist4.count(iconlist1[1])+iconlist4.count(config.icons[0])+iconlist4.count(config.icons[1])
    iconnum5 = iconlist5.count(iconlist1[1])+iconlist5.count(config.icons[0])+iconlist5.count(config.icons[1])

    match current_streak:
        case 1:
            rewards2 = icon_groups[iconlist1[1]][current_streak]
        case 2:
            rewards2 = icon_groups[iconlist1[1]][current_streak]*iconnum2
        case 3:
            rewards2 = icon_groups[iconlist1[1]][current_streak]*iconnum2*iconnum3
        case 4:
            rewards2 = icon_groups[iconlist1[1]][current_streak]*iconnum2*iconnum3*iconnum4
        case _:
            rewards2 = icon_groups[iconlist1[1]][current_streak]*iconnum2*iconnum3*iconnum4*iconnum5
    
    #第三个图标是否中奖
    if iconlist1[2] not in iconlist2 and not any(icon in iconlist2 for icon in (config.icons[1], config.icons[0])):
        current_streak = 1
    elif iconlist1[2] not in iconlist3 and not any(icon in iconlist3 for icon in (config.icons[1], config.icons[0])):
        current_streak = 2
    elif iconlist1[2] not in iconlist4 and not any(icon in iconlist4 for icon in (config.icons[1], config.icons[0])):
        current_streak =3
    elif iconlist1[2] not in iconlist5 and not any(icon in iconlist5 for icon in (config.icons[1], config.icons[0])):
        current_streak =4
    else:
        current_streak=5   

    iconnum2 = iconlist2.count(iconlist1[2])+iconlist2.count(config.icons[0])+iconlist2.count(config.icons[1])
    iconnum3 = iconlist3.count(iconlist1[2])+iconlist3.count(config.icons[0])+iconlist3.count(config.icons[1])
    iconnum4 = iconlist4.count(iconlist1[2])+iconlist4.count(config.icons[0])+iconlist4.count(config.icons[1])
    iconnum5 = iconlist5.count(iconlist1[2])+iconlist5.count(config.icons[0])+iconlist5.count(config.icons[1])

    match current_streak:
        case 1:
            rewards3 = icon_groups[iconlist1[2]][current_streak]
        case 2:
            rewards3 = icon_groups[iconlist1[2]][current_streak]*iconnum2
        case 3:
            rewards3 = icon_groups[iconlist1[2]][current_streak]*iconnum2*iconnum3
        case 4:
            rewards3 = icon_groups[iconlist1[2]][current_streak]*iconnum2*iconnum3*iconnum4
        case _:
            rewards3 = icon_groups[iconlist1[2]][current_streak]*iconnum2*iconnum3*iconnum4*iconnum5

    rewards = rewards1+rewards2+rewards3
    if rewards > 0:
       # print(f"总奖励：{rewards} 分！")
        return rewards  # 确保返回非零值，表示有奖励
    else:
        # print("没有连续图标，无奖励。")
        return 0  # 明确返回0，表示无奖励
