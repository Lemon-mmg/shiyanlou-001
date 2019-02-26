import sys
list=sys.argv[1:]
list1=[]
list2=[]
for i in list:
    if len(i)<=3:
        list1.append(i)
    elif len(i)>3:
        list2.append(i)
print(' '.join(list1))
print(' '.join(list2))