
arr = input().split()
a = int(arr[0]) 
b = int(arr[1])
c = arr[2]
if a <= 0 or b <= 0:
    print("INVALID")
else:
    print(f"{(a+b)*2} {a*b} {c.title()}")       
        