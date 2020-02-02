import math
import os
import random
import re
import sys
import operator


def deleteProducts(ids, m):
    set_ids = set(ids)
    dic_ids = {}
    for id in set_ids:
        dic_ids[id] = 0

    for id in ids:
        dic_ids[id] += 1

    # for idx, item in enumerate(dic_ids):
    #     print(item, dic_ids[item])

    sorted_x = sorted(dic_ids.items(), key=operator.itemgetter(1))

    count = 0
    for (key, value) in sorted_x:
        # print(key, value, m)
        if m >= value:
            # print("remove")
            # sorted_x.remove((key, value))
            count += 1
            m -= value
        else:
            break

    return len(sorted_x) - count



if __name__ == '__main__':
    assert(deleteProducts([1,1,1,1], 2) == 1)
    assert(deleteProducts([1,2,3,1,2,2], 3) == 1)
    assert(deleteProducts([1,2,3,4], 2) == 2)

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # ids_count = int(input().strip())
    #
    # ids = []
    #
    # for _ in range(ids_count):
    #     ids_item = int(input().strip())
    #     ids.append(ids_item)
    #
    # m = int(input().strip())
    #
    # result = deleteProducts(ids, m)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
