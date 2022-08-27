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
        self.ships = []
        self.busy = []

        self.field = [['~'] * 6 for _ in range(6)]

    def __str__(self):
        _field = ''
        _field += f'  1 2 3 4 5 6'
        for i, j in enumerate(self.field):
            _field += f'\n{i + 1} ' + ' '.join(j)
        return _field

    def add_ship(self, coords):
        for i in coords.generate_ship:
            if Dot(i.x, i.y) in self.busy:
                raise Exception
        for i in coords.generate_ship:
            self.field[i.x][i.y] = '■'
            self.busy.append(Dot(i.x, i.y))

        self.ships.append(coords)
        self._busy(coords)

    def _busy(self, coords):
        near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in coords.generate_ship:
            for _x, _y in near:
                current = Dot(i.x + _x, i.y + _y)
                if not (0 <= current.x < 6 > current.y <= 0) or current not in self.busy:
                    self.busy.append(Dot(current.x, current.y))



class Ship:
    def __init__(self, rand_coord, length):
        self.rand_coord = rand_coord
        self.length = length

    @property
    def generate_ship(self):
        ships = []

        orientation = ['U', 'D', 'L', 'R']
        while len(orientation) > 0:
            for i in range(self.length):
                x = self.rand_coord.x
                y = self.rand_coord.y
                if orientation[0] == 'U':
                    y -= i
                elif orientation[0] == 'D':
                    y += i
                elif orientation[0] == 'L':
                    x -= i
                elif orientation[0] == 'R':
                    x += i
                if 0 <= x < 6 > y >= 0:
                    ships.append(Dot(x, y))
                else:
                    break
            if len(ships) == self.length:
                return ships
            else:
                orientation = orientation[1:]


class Game:

    def do_it_till_not_generate(self):
        board = None
        while board is None:
            board = self.rand_ships()
        return board

    def rand_ships(self):
        board = Board()
        retry = 1
        len_of_ships = [3, 2, 2, 1, 1, 1, 1]
        for i in len_of_ships:
            while True:
                retry += 1
                if retry > 2000:
                    return None
                ship = Ship(Dot(randint(0, 5), randint(0, 5)), i)
                try:
                    board.add_ship(ship)
                    break
                except Exception:
                    pass
        return board

b = Game()
print(b.do_it_till_not_generate())
