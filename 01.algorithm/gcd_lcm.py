from math import gcd

a = [2, 6]
b = [16, 32, 96]
# b = [24, 36]

# 최대공약수 직접 구현
# 유클리드호제법
def gcd_my(a, b):
    if b == 0:
        return a
    else:
        return gcd_my(b, a%b)

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

print(gcd_my(16, 32)) # 16
print(gcd_my(16, 96)) # 16

print(gcd_array(b))
print(lcm(2, 6))
print(lcm_array(a))
print(lcm_array(b))