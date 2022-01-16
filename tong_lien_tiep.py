import math
t = int(input())
while t:
    t -= 1
    n = int(input()) *2
    dem = 0
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            j = n / i
            if i != j and (j-i-1) % 2 == 0 and (j+i+1) % 2 == 0:
                dem+=1
    print(dem)