def max2(a):
    max_num=max(a)
    a.remove(max_num)
    return max(a)

# a=[8,4,6,3,2,7,2,1,0,6]
a=list(map(int,input().split()))
print(max2(a))








# a=[8,4,6,3,2,7,2,1,0,6]
# max=max(a)
# a.remove(max)
# print(max(a))