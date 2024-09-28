def Remove(duplicate):
    final_list=[]
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
            return final_list
        duplicate=[2,3,4,5,2,3,1]
       
        print(Remove(duplicate))