def test():
    try:
        
        n = int(input())
        if (n%2 == 0):
            print("Invalid Input")
            return 0
        arr = [int(i) for i in input().split()]
        for i in range(n):
            found = 0
            for j in range(n):
                if i == j:
                    continue
                if arr[i] == arr[j]:
                    found = 1
                    break
            if found == 0:
                print(arr[i])
                break
    except:
        print("Invalid Input")
test()