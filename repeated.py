try:

    n = int(input())
    arr = [int(i) for i in input().split()]
    repeat = set()
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                repeat.add(arr[i])
    if len(repeat):
        print(" ".join(str(i) for i in repeat))
    else:
        print("unique")
except:
    print("Invalid Input")
