def add2list(lst1,lst2):
    new_list = [lst1[index] + lst2[index] for index in range(len(lst1))]
    return (new_list)

lst1 = [2,3,4]
lst2 = [2,1,0]
ans = add2list(lst1,lst2)
print(ans)