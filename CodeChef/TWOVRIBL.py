import time

start = time.time()

max_num = 100000
lst_count = [0]*max_num
y = [0]*max_num
lst_count[1] = 1
y[1] = 1
lst_count[2] = 2
y[2] = 5

x = 3

while x < max_num:
    val = x*x
    check = 1
    
    while True:
        if y[x-check] < val:
            lst_count[x] = lst_count[x-check] + 1
            y[x] = y[x-check] + val
            break
        else:
            check += 1
        
    x += 1

end = time.time()
print(end - start)

# T = int(input())
# for i in range(T):
#     ch = int(input())
#     print(lst_count[ch])