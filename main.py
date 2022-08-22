from random import randint

letters = 'ABCDEF'
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Board:

    def __init__(self):
        self.field = [['~'] * 6 for i in range(6)]

    def __str__(self): # создать список для доски для ретурна
        print(f'  1 2 3 4 5 6')
        for i, j in enumerate(self.field):
            print(f'{letters[i]} ' + ' '.join(j))
        return ''


class Ship:
    coords_of_ships = []
    def __init__(self):
        pass

    def rand_ship(self, rnd_coords, ship, orientation):
        # board = Board()
        self.x = rnd_coords.x
        self.y = rnd_coords.y
        for i in range(ship):
            if i == 0:
                self.coords_of_ships.append([self.x, self.y])
                continue
            if 0 <= self.x <= 5 and 0 <= self.y <= 5:
                if orientation:
                    self.x += 1
                else:
                    self.y += 1
                self.coords_of_ships.append([self.x, self.y])
        return self.coords_of_ships

        # return False


class Game:
    def __init__(self):
        pass

    def rand_coord(self):
        board = Board()
        # board.field[randint(0, 5)][randint(0, 5)] = '■'
        ship = Ship()
        _ships_ = [3, 2, 2, 1, 1, 1]
        for _ship_ in _ships_:
            rnd_coord = Dot(randint(0, 5), randint(0, 5))
            orientation = randint(0, 1)
            ship.rand_ship(rnd_coord, _ship_, orientation)
        for crd in ship.coords_of_ships:
            board.field[crd[0]][crd[1]] = '■'
        return board


    def play(self):
        pl = input(': ')
        if pl[0] in letters:
            x = int(letters.index(pl[0]))
            y = int(pl[1])
            b.field[x][y - 1] = '■'
        return ''

# b = Board()
# b.field[4][5] = '■'
# print(b.make_board())
#
# a = Game()
# print(a.play())
# print(b)

b = Game()
print(b.rand_coord())
