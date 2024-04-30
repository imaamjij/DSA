def dup(a):
    arr=[]
    for i in a:
        if i not in arr:
            arr.append(i)

    print(arr)

a=list(map(int,input().split()))
dup(a)