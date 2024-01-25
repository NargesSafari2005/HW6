import numpy as np
import re


class Soldier :
    def __init__(self, soldier_id, x, y) :
        self.id = soldier_id
        self.x = x
        self.y = y
        self.health = 100

    def display_info(self) :
        print(f'health: {self.health}\nlocation: {self.x} {self.y}')


class Melee(Soldier) :
    def __init__(self, soldier_id, x, y) :
        super().__init__(soldier_id, x, y)
        self.damage = 20


class Archer(Soldier) :
    def __init__(self, soldier_id, x, y) :
        super().__init__(soldier_id, x, y)
        self.damage = 10


# Patterns:
create_soldier = r"^new\s(melee|archer)\s([0-9]|[1-4][0-9]|49)\s([0-9]|[1-9][0-9]|100)\s([0-9]|[1-9][0-9]|100)$"
move = r"^move\s([0-9]|[1-4][0-9]|49)\s(up|down|left|right)$"
attack = r"^attack\s([0-9]|[1-4][0-9]|49)\s([0-9]|[1-4][0-9]|49)$"
info = r"^info\s([0-9]|[1-4][0-9]|49)$"
status = r"who is in the lead?"
end = r"end"


def move_soldier(soldier, direction, n) :
    if direction == 'down' and soldier.y < (n - 1) :
        soldier.y += 1
    elif direction == 'up' and soldier.y > 0 :
        soldier.y -= 1
    elif direction == 'right' and soldier.x < (n - 1) :
        soldier.x += 1
    elif direction == 'left' and soldier.x > 0 :
        soldier.x -= 1
    else :
        print('out of bounds')
        return False
    return True


def h_distance(x1, y1, x2, y2) :
    return abs(x2 - x1) + abs(y2 - y1)


n = int(input())

soldiers = np.empty((2, 50), dtype=object)
soldiers[:] = None
turn = 0

while True :
    turn %= 2
    command = input()
    command_list = command.split()

    if re.match(end, command) :
        break
    elif re.match(create_soldier, command) :
        if soldiers[turn][int(command_list[2])] is not None :
            print('duplicate tag')
            continue

        if command_list[1] == 'melee' :
            soldier = Melee(int(command_list[2]), int(command_list[3]), int(command_list[4]))
        else :
            soldier = Archer(int(command_list[2]), int(command_list[3]), int(command_list[4]))

        soldiers[turn][int(command_list[2])] = soldier

    elif re.match(move, command) :
        soldier = soldiers[turn][int(command_list[1])]
        done = move_soldier(soldier, command_list[2], n)
        if not done :
            continue

    elif re.match(attack, command) :
        attacker = soldiers[turn][int(command_list[1])]
        target = soldiers[(turn + 1) % 2][int(command_list[2])]
        distance = h_distance(attacker.x, attacker.y, target.x, target.y)

        if isinstance(attacker, Melee) and distance <= 1 :
            target.health -= attacker.damage
        elif isinstance(attacker, Archer) and distance <= 2 :
            target.health -= attacker.damage
        else :
            print('the target is too far')
            continue

        if target.health <= 0 :
            soldiers[(turn + 1) % 2][int(command_list[2])] = None
            print('target eliminated')

    elif re.match(info, command) :
        if soldiers[turn][int(command_list[1])] is None :
            print('soldier does not exist')
            continue
        else :
            soldiers[turn][int(command_list[1])].display_info()

    elif re.match(status, command) :
        player1 = sum(s.health for s in soldiers[0] if s is not None)
        player2 = sum(s.health for s in soldiers[1] if s is not None)

        if player1 > player2 :
            print('player 1')
        elif player2 > player1 :
            print('player 2')
        else :
            print('draw')
        continue

    else :
        continue

    turn += 1
