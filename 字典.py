a_list=[1,2,3,4,5,6]
# 字典，类似于map，内部无顺序,很灵活，可以在字典里再套字典
d={'apple':1,'pear':2,'orange':3,'new':{3:0,2:1}} #前一个是key，后一个是所对应内容
d2={1:'a','c':'b'}
print(d['apple'])

del d['pear'] #删除一个元素
d['b']=20 # 新增元素

print(d['new'][2])
