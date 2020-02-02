# -'- coding: utf-8 -*-
import sys
import json
from random import choice


def main():
    '''
        인풋은 json형식으로 들어오며
        'map' : 8 * 8 크기의 판의 상태를 한 칸당 한 글자로 공백없이 string의 형태로 준다.
        'opponent_history' : 지금까지 상대가 움직인 방향들을 string의 형태로 공백없이 준다. ex) 'UDDLLUR'
        'my_history' : 지금까지 내가 움직인 방향들을 string의 형태로 공백없이 준다.        ex) 위와 동일
        'me' : 내가 누군지 알려줌.          ex) 'A' or 'B'
        'opponent' : 상대가 누군지 알려줌.  ex) 위와 동일

	map에 대한 상세한 설명
	💎 : 갈 수 있는 곳입니다. 젬이라고 불리죠
	A, B : 위에서 설명했듯 인풋중 me로 들어온 알파벳이 본인이 움직일 말이 됩니다.
	a, b : A, B가 이미 지나간 길, 다시 말해 다시는 갈 수 없는 길입니다.
    '''

    data = json.loads(sys.argv[1])

    map_string = data['map']
    opponent_history = data['opponent_history']
    my_history = data['my_history']
    player = data['me']
    opponent = data['opponent']

    # 재미를 위해 젬을 직접 이용해서 코드를 짜보세요!
    new_input_str = map_string.replace("*", "💎")

    map = []

    for i in range(8):
        map.append(list(map_string[8 * i:8 * i + 8]))

    # TODO: 아래쪽을 변경하여 멋진 코드를 만들어 주세요!

    available = ['U', 'D', 'R', 'L']
    print(choice(available))


main()