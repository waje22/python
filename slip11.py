t1=(1,2,3,4)
t2=(3,4,5,6)
t3=(2,3,6,5)
print("original list:")
print(t1)
print(t2)
print(t3)
print("element wise sum of the said tuples")
result=tuple(map(sum,zip(t1,t2,t3)))
print(result)
list1=[1,5,7]
list2=[3,2,1]
t1=(list1)
t2=(list2)
print(t1+t2)