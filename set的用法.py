char_list=['a','b','b','c','c','c']
#print(char_list)

unique_char=set(char_list)
print(unique_char)

unique_char.add('x')
print(unique_char)

set1=unique_char
set2={'a','e','i'}
print(set1.difference(set2)) #输出set1和set2的差
print(set1.intersection(set2)) #输出set1和set2的交集
