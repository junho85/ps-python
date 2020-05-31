apple = 130

house_left = 100
house_right = 200

if house_left <= apple <= house_right:
    print("apple is in the house")
else:
    print("apple is not in the house")


if house_left <= apple and apple <= house_right:
    print("apple is in the house")
else:
    print("apple is not in the house")


