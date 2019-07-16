try:
    file=open('eee','r+')
except Exception as e:
    print('there is no file named as eee')
    response=input('Do you want to create a new file?(y/n)')
    if response=='y':
        file=open('eee','w')
    else:
        pass
else:
    file.write('ssss') #对应上方的try
file.close()
