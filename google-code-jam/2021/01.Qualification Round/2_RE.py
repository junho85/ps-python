tc = int(input())


def solve(X, Y, arts):
    arts = list(arts)
    prefer = X < Y # True CJ, False JC
    result = 0
    for i in range(len(arts)):
        if arts[i] == '?':
            if i == 0:
                right = arts[i + 1]
                if right == 'C':
                    arts[i] = 'C'
                elif right == 'J':
                    arts[i] = 'J'
                else: # '?'
                    # ? 아닌거 찾아서 전부 같은거로 바꾸기
                    be = None
                    j = 0
                    for j in range(i, len(arts)):
                        if arts[j] == '?':
                            continue
                        else:
                            be = arts[j]
                    for k in range(i, j+1):
                        arts[k] = be
            elif i == len(arts) - 1:
                left = arts[i - 1]
                if left == 'C':
                    arts[i] = 'C'
                else:
                    arts[i] = 'J'
            else:
                left = arts[i-1]
                right = arts[i+1]

                if left == right:
                    arts[i] = left
                else:
                    # prefer CJ - CJ or JJ
                    if prefer:
                        arts[i] = 'J'
                    # prefer JC - JC or CC
                    else:
                        arts[i] = 'C'
        if i != 0:
            left = arts[i-1]
            right = arts[i]

            if left == 'C' and right == 'J':
                result += X
            elif left == 'J' and right == 'C':
                result += Y


    return result


for t in range(1, tc+1):
    (X, Y, arts) = input().split()
    X = int(X)
    Y = int(Y)

    ans = solve(X, Y, arts)
    print("Case #" + str(t) + ": " + str(ans))
