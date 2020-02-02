def get_middle(str):
    center = int(len(str)/2)
    if len(str)%2 == 1:
        return str[center]
    else:
        return str[center-1:center + 1]

print(get_middle('i'))
print(get_middle('pycon'))
print(get_middle('aone'))