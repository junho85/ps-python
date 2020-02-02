# -'- coding: utf-8 -*-
import sys
import subprocess
import json
from random import choice


def main():
    file_name = sys.argv[1]

    # 예시 인풋 두개
    data_list = [{'map': 'A**************************************************************B',
                  'opponent_history': '', 'my_history': '', 'me': 'A', 'opponent': 'B'},
                 {'map': 'aA************************************************************Bb',
                  'opponent_history': 'R', 'my_history': 'L', 'me': 'B', 'opponent': 'A'}]

    data_str = json.dumps(choice(data_list))

    out = subprocess.check_output([sys.executable, file_name, data_str]).decode().strip()
    direction = str(out)

    right = ['U', 'D', 'R', 'L']

    if direction in right:
        print("You choose {}".format(direction))
    else:
        print("Wrong form")

main()