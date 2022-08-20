from random import randint

coord = ['A', 'B', 'C', 'D', 'E', 'F']

board = [{coord[j] + str(i + 1): '░'} for i in range(6) for j in range(6)]
game = board.copy()
def make_board(game):
    print(f'  A B C D E F')
    cnt = 0
    for i in range(6):
        print(i + 1,
              game[cnt].get('A' + str(i + 1)),
              game[cnt + 1].get('B' + str(i+1)),
              game[cnt + 2].get('C' + str(i + 1)),
              game[cnt + 3].get('D' + str(i + 1)),
              game[cnt + 4].get('E' + str(i + 1)),
              game[cnt + 5].get('F' + str(i + 1)))
        for j in range(6):
            cnt += 1
        # print(cnt)
# print('■')
# for i in range(6):
#      print(*board[i], end=' ')
# print(board)

print(make_board(game))

player = input(': ')
for i in game:
    i[player] = 'X'

print(make_board(game))
