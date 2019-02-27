try:
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr = sorted(arr, reverse = True)
        
    x = "".join(str(i) for i in arr)
    print(int(x))
except:
    print("Invalid Input")