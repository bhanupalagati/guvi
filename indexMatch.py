try:
    n = int(input())
    arr = [int(i) for i in input().split()]
    s = ""
    for i in range(len(arr)-1):
        if i == arr[i]:
            s+=str(i)+" "
    if len(arr)-1 == arr[-1]:
        s+=str(arr[-1])+'.'
    print(s)
except:
    print("Invalid Input")