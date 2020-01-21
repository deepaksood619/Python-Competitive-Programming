from fractions import Fraction

prime_numbers_60 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]

def print_val(total_bad_num, total_good_num):
    if total_bad_num != 0 and total_good_num != 0:
        lowest = str(Fraction(total_bad_num, total_good_num))
        print(lowest.replace('/', ':'))
    else:
        print('{}:{}'.format(total_bad_num, total_good_num))
        
def increment_time(input_time):
    time = list(input_time)
    if time[2] < 59:
        time[2] += 1
    elif time[1] < 59:
        time[1] += 1
        time[2] = 0
    else:
        time[0] += 1
        time[1] = 0
        time[2] = 0
        
    return tuple(time)

def calculate_good_bad(current_time):
    total_bad_num = 0
    total_good_num = 0
    
    if current_time in cache_dict:
        return cache_dict[current_time][0], cache_dict[current_time][1]
    else:
        incremented_time = increment_time(current_time)
        total_bad_num, total_good_num = calculate_good_bad(incremented_time)
        
        primes = set([num for num in current_time if num in prime_numbers_60])
        
        bad_num_bool = False
        for prime in primes:
            bad_num = 0
            for num in current_time:
                if num%prime == 0:
                    bad_num += 1

            if bad_num == 3:
                bad_num_bool = True
                break

        if bad_num_bool:
            total_bad_num += 1
        else:
            total_good_num += 1

        cache_dict[current_time] = [total_bad_num, total_good_num]
        
        return total_bad_num, total_good_num
        
t = int(input())

cache_dict = {(23,59,59): [0, 1]}

for _ in range(t):
    input_time = tuple(map(int, input().split()))
    
    total_bad_num, total_good_num = calculate_good_bad(input_time)
        
    print_val(total_bad_num, total_good_num)
