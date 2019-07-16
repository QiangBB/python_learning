import pickle

a_dict={'time':'','version':1}

file=open('pickle_example.pickle','wb')
pickle.dump(a_dict,file)
file.close()
    
with open('pickle_example.pickle','rb') as file:
    a_dict1=pickle.load(file)

print(a_dict1)
