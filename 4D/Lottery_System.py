
# 马来4d开奖计算复合投注号码的中奖等级和中奖数量
# 初始化一个标志，假设我们期望用户输入"e"来结束循环
def get_input(inname):
    temnumlist = []
    continue_input = 1
    i = 1
    while continue_input == 1:
        # 获取用户输入
        
        print("请输入第",i,"个",inname,"号码（输入'E'以结束）: ")
        i = i+1
        user_input = input()
        
        # 判断用户输入是否为'E'
        if user_input == "E":
            continue_input = 0  # 如果输入'E'，则改变标志为False，循环将终止
        else:
            # 这里可以添加处理用户输入的逻辑
            temnumlist.append(user_input)
    return temnumlist

#存储下注号码
numlist = get_input("下注")
#存储中奖号码
sj = get_input("头三奖")
tbj = get_input("特别奖")
anj = get_input("安慰奖")

#存储所有下注号码组合
numlist2 = []
for i in range(len(numlist)) :
    for j in range(len(numlist)-i) :
        if numlist[i] != numlist[i+j] :
            numlist2.append([numlist[i],numlist[i+j]]) 

#存储中奖号码数组            
zj1 = []
zj2 = []
zj3 = []
zj4 = []
zj5 = []

#计算中奖号码
len1 =len(numlist2)
for i in range(len1):
    if numlist2[i][0] in sj :
        if numlist2[i][1] in sj :
            zj1.append(numlist2[i])
        elif numlist2[i][1] in tbj :
            zj2.append(numlist2[i])
        else :
            zj3.append(numlist2[i])
    elif numlist2[i][0] in tbj :
        if numlist2[i][1] in sj :
            zj2.append(numlist2[i])
        else :
            zj4.append(numlist2[i])
    elif numlist2[i][0] in anj :
        if numlist2[i][1] in sj :
            zj3.append(numlist2[i])
        else :
            zj5.append(numlist2[i])
    else :
        if numlist2[i][1] in sj :
            zj3.append(numlist2[i])
        else :
            wzj = +1

#输出中奖结果
print("首奖有",len(zj1),"注",zj1)
print("2奖有",len(zj2),"注",zj2)
print("3奖有",len(zj3),"注",zj3)
print("4奖有",len(zj4),"注",zj4)
print("5奖有",len(zj5),"注",zj5)