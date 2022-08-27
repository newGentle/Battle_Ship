from random import randint

class GameException(Exception):
    pass
class BoardErrorException(GameException):
    pass

class OutOfBoardException(GameException):
    def __repr__(self):
        return f'Командир, стрельба вне зоны...'

class SamePointException(GameException):
    def __repr__(self):
        return f'Командир, мы туда снаряд отправляли уже...'
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'{self.x}, {self.y}'

class Board:

    def __init__(self, hide=False):
        self.ships = []
        self.busy = []
        self.count = 0
        self.field = [['~'] * 6 for _ in range(6)]
        self.hide = hide
        self.letters = 'ABCDEF'
    def __str__(self):
        _field = ''
        _field += f'  1 2 3 4 5 6'
        for i, j in enumerate(self.field):
            _field += f'\n{self.letters[i]} ' + ' '.join(j)
        if self.hide:
            _field = _field.replace('■', '~')
        return _field

    def add_ship(self, coords):
        for i in coords.generate_ship:
            if Dot(i.x, i.y) in self.busy:
                raise BoardErrorException
        for i in coords.generate_ship:
            self.field[i.x][i.y] = '■'
            self.busy.append(Dot(i.x, i.y))

        self.ships.append(coords)
        self._busy(coords)

    def _busy(self, coords, verb=False):
        near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in coords.generate_ship:
            for _x, _y in near:
                current = Dot(i.x + _x, i.y + _y)
                if (0 <= current.x < 6 > current.y >= 0) and current not in self.busy:
                    if verb:
                        self.field[current.x][current.y] = '.'
                    self.busy.append(current)

    def shot(self, d):
        if not (0 <= d.x < 6 > d.y >= 0):
            raise OutOfBoardException()

        if d in self.busy:
            raise SamePointException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.generate_ship:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self._busy(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False
    def begin(self):
        self.busy = []
class Ship:
    def __init__(self, rand_coord, length):
        self.rand_coord = rand_coord
        self.length = length
        self.lives = length

    @property
    def generate_ship(self):
        orientation = ['U', 'D', 'L', 'R']
        while len(orientation) > 0:
            ships = []
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
    def shooten(self, shot):
        return shot in self.generate_ship
class Player:
    def __init__(self, board, opponent):
        self.letters = 'ABCDEF'
        self.board = board
        self.opponent = opponent
    def ask(self):
        raise NotImplementedError()

    def turn(self):
        while True:
            try:
                target = self.ask()
                repeat = self.opponent.shot(target)
                return repeat
            except GameException as e:
                print(e)

class Computer(Player):
    def ask(self):
        aim = Dot(randint(0, 5), randint(0, 5))
        print(f'Выстрел врага - {self.letters[aim.x]}{aim.y + 1}')
        return aim
class User(Player):

    def ask(self):
        while True:
            aim = input('Командир, введите координаты: ')
            if not aim:
                continue
            if aim[0] in self.letters and aim[1].isdigit() and (0 < int(aim[1]) <= 6):
                _x = int(self.letters.index(aim[0]))
                _y = int(aim[1]) - 1
            else:
                print('Командир, координаты не верны')
                continue
            return Dot(_x, _y)

class Game:

    def __init__(self):
        user = self.do_it_till_not_generate()
        computer = self.do_it_till_not_generate()
        computer.hide = True

        self.ai = Computer(computer, user)
        self.usr = User(user, computer)

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
                except BoardErrorException:
                    pass
        board.begin()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" пример ввода: A2  ")
        print(" A - номер строки  ")
        print(" 2 - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Наша поля:")
            print(self.usr.board)
            print("-" * 20)
            print("Поля врага:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 20)
                print("Наш Ход!")
                repeat = self.usr.turn()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.turn()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 20)
                print("Командир, Победа за нами!")
                break

            if self.usr.board.count == 7:
                print("-" * 20)
                print("Враг выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

b = Game()
b.start()


