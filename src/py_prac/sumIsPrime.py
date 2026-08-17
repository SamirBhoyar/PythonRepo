def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def check_sum_prime(nums):
    res = []
    for n in nums:
        s = sum(int(d) for d in str(n))
        res.append('Yes' if is_prime(s) else 'No')
    print(', '.join(res))

# example usage
check_sum_prime([123, 47])