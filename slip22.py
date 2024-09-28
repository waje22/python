list=[12,11,6,5,7,9,7,5,4,3,2]
cnt=len(list)
for i in range(0,cnt-1):
    for j in range(0,cnt-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
            print(list)