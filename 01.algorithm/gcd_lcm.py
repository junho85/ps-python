from math import gcd

# 최대공약수 직접 구현

# 유클리드호제법 recursive
def gcd_my(a, b):
    if b == 0:
        return a
    else:
        return gcd_my(b, a % b)


# 유클리드호제법 while loop
def gcd_my2(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


# 배열의 최대공약수
def gcd_array(arr):
    gcd_arr = None
    for i in range(len(arr)):
        if i == 0:
            gcd_arr = arr[i]
        else:
            gcd_arr = gcd(gcd_arr, arr[i])
    return gcd_arr

# 최소공배수
def lcm(a, b):
    return int(a * b / gcd(a, b))

# 배열의 최소공배수
def lcm_array(arr):
    lcm_arr = None
    for i in range(len(arr)):
        if i == 0:
            lcm_arr = arr[i]
        else:
            lcm_arr = lcm(lcm_arr, arr[i])
    return lcm_arr

print("== gcd ==")
assert(gcd(4, 6) == 2)
assert(gcd(6, 4) == 2)
assert(gcd(16, 32) == 16)
assert(gcd(16, 96) == 16)

print("== gcd_my ==")
assert(gcd_my(4, 6) == 2)
assert(gcd_my(6, 4) == 2)
assert(gcd_my(16, 32) == 16)
assert(gcd_my(16, 96) == 16)

print("== gcd_my2 ==")
assert(gcd_my2(4, 6) == 2)
assert(gcd_my2(6, 4) == 2)
assert(gcd_my2(16, 32) == 16)
assert(gcd_my2(16, 96) == 16)

assert(gcd_array([16, 32, 96]) == 16)
assert(lcm(2, 6) == 6)
assert(lcm_array([2, 6]) == 6)
assert(lcm_array([16, 32, 96]) == 96)