#!/usr/bin/env python3

import json
import sys
import random

my_action_history = []

def action(what):
    if what not in ('idle', 'forward', 'backward', 'punch', 'kick',
                    'crouch', 'jump', 'guard'):
        raise ValueError(f'Unknown action type: {what}')
    my_action_history.append(what)
    sys.stdout.write(what + '\n')
    sys.stdout.flush()


def read_status():
    data = sys.stdin.readline()
    while data:
        yield json.loads(data)
        data = sys.stdin.readline()


attack_type = {
    0: 'kick',
    1: 'punch',
}
attack_count = 0

guard_type = {
    0: 'crouch',
    1: 'jump',
    2: 'guard',
}
guard_count = 0

forward_type = {
    0: 'forward',
    1: 'idle',
}
forward_count = 0


def guard():
    action(guard_type.get(guard.count % len(guard_type)))
    guard.count += 1


def forward():
    action(forward_type.get(forward.count % len(forward_type)))
    forward.count += 1


def attack():
    action(attack_type.get(attack.count % len(attack_type)))
    attack.count += 1


guard.count = 0
forward.count = 0
attack.count = 0


def attack_and_guard():
    if random.randint(0, 1):
        attack()
    else:
        guard()

opponent_action_history = []


def examine_opponent_action_pattern():
    recent_actions = opponent_action_history[-4:]
    # print(recent_actions, file=sys.stderr)
    if len(set(recent_actions)) == 1: # all same
        if recent_actions[0] == 'Action.punch':
            return 'simple_punch'
        elif recent_actions[0] == 'Action.kick':
            return 'simple_kick'
    elif recent_actions == ['Action.punch', 'Action.kick', 'Action.punch', 'Action.kick']:
        return 'punch_kick_punch_kick'
    elif recent_actions == ['Action.kick', 'Action.punch', 'Action.kick', 'Action.punch']:
        return 'kick_punch_kick_punch'
    else:
        return 0



for status in read_status():
    distance = status['distance']
    time_left = status['time_left']
    health = status['health']
    opponent_health = status['opponent_health']
    opponent_action = status['opponent_action']
    given_damage = status['given_damage']
    taken_damage = status['taken_damage']
    match_records = status['match_records']

    opponent_action_history.append(opponent_action)

    # if len(my_action_history) != 0:
    #     print("my action was " + my_action_history[-1], file=sys.stderr)

    # 아래 코드를 수정해 주세요!
    if distance == 0:
        pattern = examine_opponent_action_pattern()
        # print("pattern is " + str(pattern), file=sys.stderr)

        # attack()
        if pattern == 'simple_punch':
            attack()
        elif pattern == 'simple_kick':
            attack()
        elif pattern == 'punch_kick_punch_kick':
            print("punch_kick_punch_kick", file=sys.stderr)
            # next will be punch
            if my_action_history[-1] == 'crouch' or my_action_history[-1] == 'jump' or my_action_history[-1] == 'guard':
                print("do kick!", file=sys.stderr)
                action('kick')
            else:
                print("do crouch!", file=sys.stderr)
                action('crouch')
        elif pattern == 'kick_punch_kick_punch':
            print("kick_punch_kick_punch", file=sys.stderr)
            # next will be kick
            if my_action_history[-1] == 'crouch' or my_action_history[-1] == 'jump' or my_action_history[-1] == 'guard':
                print("do kick!", file=sys.stderr)
                action('kick')
            else:
                action('jump')
        else: # don't know pattern
            print("don't know pattern", file=sys.stderr)
            attack()
    else:
        forward()
