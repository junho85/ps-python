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
    0: 'punch',
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
    if len(set(recent_actions)) == 1: # all same
        if recent_actions[0] == 'punch':
            return 'simple_punch'
        elif recent_actions[0] == 'kick':
            return 'simple_kick'
    elif recent_actions == ['punch', 'kick', 'punch', 'kick']:
        return 'punch_kick_punch_kick'
    elif recent_actions == ['kick', 'punch', 'kick', 'punch']:
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

    # 아래 코드를 수정해 주세요!
    if distance == 0:
        attack()
    else:
        forward()
