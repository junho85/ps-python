# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

def adjacentElementsProduct(inputArray):
    max = inputArray[0] * inputArray[1]

    for idx in range(1, len(inputArray) - 1):
        temp = inputArray[idx] * inputArray[idx + 1]
        if temp > max:
            max = temp
    return max

assert(adjacentElementsProduct([3, 6, -2, -5, 7, 3]) == 21)