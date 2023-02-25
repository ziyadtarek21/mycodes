import pygame, sys, time
import numpy as np

pygame.init()
width = 600
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Two squares')
screen.fill('black')
# pygame.draw.line(screen,'orange',(10,10),(300,300),10)
board = np.zeros((4, 4))
print(board)


def draw_lines():
    # horizontal lines
    for x in range(3):
        pygame.draw.line(screen, "orange", (0, 150 + 150 * x), (600, 150 + 150 * x), 10)

    # pygame.draw.line(screen, 'orange', (0, 550), (800, 550), 10)
    # vertical
    for v in range(3):
        pygame.draw.line(screen, 'orange', (150 + 150 * v, 0), (150 + 150 * v, 600), 10)

    # pygame.draw.line(screen, 'orange', (550,0), (550, 800), 10)


font = pygame.font.Font(None, 90)
font1 = pygame.font.Font(None, 60)

def drawnum(nums, temp_nums):
    for y in range(4):
        for x in range(4):
            if x + y * 4 in nums or x + y * 4 in temp_nums:
                # go to the next loop
                continue
            text = font.render(str(1 + x + y * 4), True, 'orange')
            screen.blit(text, (65 + 150 * x, 25 + 150 * y))


def mark_square(row, col, player):
    board[row][col] = player


def avilable_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def isboard_full():
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                return False
    return True


def wining(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0 and (j + 1) % 4 != 0:
                if board[i][j + 1] == 0:
                    return 1
            if board[i][j] == 0 and (i + 1) % 4 != 0:
                if board[i + 1][j] == 0:
                    return 1
    return 0


player = 1
nums = set()
temp_nums = []
while True:
    screen.fill('black')
    draw_lines()
    drawnum(nums, temp_nums)
    # f is to put variable in a string
    turn_text = font1.render(f"player {player}'s turn", True, "White")
    screen.blit(turn_text, (170, 630))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mousex = pygame.mouse.get_pos()[0]
                mousey = pygame.mouse.get_pos()[1]
                clicked_row = int(mousey // 150)
                clicked_column = int(mousex // 150)
                if clicked_row > 3:
                    continue
                # to check that the chosen number is unrepeated
                if clicked_column + clicked_row * 4 in nums or clicked_column + clicked_row * 4 in temp_nums:
                    continue
                temp_nums.append(clicked_column + clicked_row * 4)
                temp_nums.sort()
                mark_square(clicked_row, clicked_column, player)
                if len(temp_nums) == 2:
                    if (temp_nums[1] - temp_nums[0] not in [1, 4]):
                        temp_nums.pop()
                        continue
                    for x in temp_nums:
                        nums.add(x)
                    temp_nums = []
                    if not wining(board):
                        screen.fill("Black")
                        winning_text = font.render(f"Player {player} Won", True, "Red")
                        screen.blit(winning_text, (110, 350))
                        pygame.display.update()
                        time.sleep(3)
                        pygame.quit()
                    if player == 1:
                        player = 2
                    else:
                        player = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex = event.pos[0]
            mousey = event.pos[1]
            clicked_row = int(mousey // 150)
            clicked_column = int(mousex // 150)

    pygame.display.update()