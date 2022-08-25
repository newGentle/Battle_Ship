from random import randint


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'{self.x}, {self.y}'

class Board:
    def __init__(self):
        self.field = [['~'] * 6 for _ in range(6)]

    def __str__(self):
        _field = ''
        _field += f'  1 2 3 4 5 6'
        for i, j in enumerate(self.field):
            _field += f'\n{i + 1} ' + ' '.join(j)
        return _field

def check_dots(dots):
    if not (0 <= dots.x < 6 > dots.y >= 0):
        return False
    return True

def safe_dots(dots):
    safe_zone = []
    safe = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)]
    for _x, _y in safe:
        cur = Dot(_x + dots.x, _y + dots.y)
        if 0 <= cur.x < 6 > cur.y >= 0:
            safe_zone.append(Dot(cur.x, cur.y))
    return safe_zone

appended_coords = []
new_ship_coords = []
len_of_ships = [3, 2, 2, 1, 1, 1, 1]
for i in len_of_ships:
    while len(new_ship_coords) < i:
        ship = Dot(randint(0, 5), randint(0, 5))
        orientation = randint(0, 1)
        if 0 <= ship.x < 6 > ship.y >= 0:
            for j in range(i):
                x = ship.x
                y = ship.y
                if orientation:
                    x += j
                else:
                    y += j

                if check_dots(Dot(x, y)):
                    new_ship_coords.append(Dot(x, y))
                else:
                    new_ship_coords = []
                    break
        else:
            continue
    for z in new_ship_coords:
        appended_coords.append(Dot(z.x, z.y))
    new_ship_coords = []


x = Board()
try:
    for i in appended_coords:
        z = safe_dots(Dot(i.x, i.y))
        for j in z:
            x.field[j.x][j.y] = '.'
            x.field[i.x][i.y] = '■'
except Exception as e:
    print(j.x, j.y)

print(x)
print(len(appended_coords))
