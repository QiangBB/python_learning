# tuple list

a_tuple=(12,3,5,15,6)
another_tuple=2,4,6,7,8

a_list=[12,3,6,7,8]

for index in range(len(a_list)):
    print('index=',index,'number in list',a_list[index])
    
# 列表的深入
a =[1,2,3,4,5,3]
a.append(0) # 在列表末尾加0
a.insert(1,0)# 第一个参数是添加位置(从0开始)，第二个参数是添加的数值
a.remove(2) # 参数是所要移除的数值
print(a)
print(a[-1]) #输出列表的最后一位,-2表示倒数第二位
print(a[2:4]) #输出列表中索引为2,3的数值
print(a.index(3)) #输出列表中值为2的第一个索引
print(a.count(2)) #输出列表中出现2的次数

a.sort(reverse=True) #默认是从小到大,参数传入reverse=True为从大到小
print(a)

