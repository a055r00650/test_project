my_dict = {} #空字典

x,y = range(2, 10), range(2, 10) 
for a in x :
    for b in y:
        i = str(a) + str(b) #未相乘的值 當字串相加，使用i存起來，然後用來當key
        my_dict[i] = a * b  #相乘後的值 存在當前i key 下的 value

for i, j in my_dict.items():
    #使用i變數，取出dict中的key值，並使用j變數，來取出當前key內的value
    print(f"{i}: {j}", end="\t")
    if i.endswith('9'): 
    #使用.endswith()字符串方法`，檢查key的字尾是否為9
        print()

