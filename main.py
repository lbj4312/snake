import pygame, sys
import random

# 初始化
pygame.init()
fclock = pygame.time.Clock()
fps = 1
font = pygame.font.Font('fz.TTF', 50)

# 设置背景音乐
pygame.mixer.music.load("music\背景音乐.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)

# 加载得分音效
eat_sound = pygame.mixer.Sound("music\吃.mp3")
eat_sound.set_volume(0.2)

# 创建分数
score = 3

# 屏幕对象
screen = pygame.display.set_mode((800, 600))  # 尺寸

# 贪吃蛇列表
snake_list = [[20, 20], [20, 40], [20, 60]]

# 初始方向
direction = 'right'

# 食物
food = [random.randint(1, 39) * 20, random.randint(1, 29) * 20]

# 游戏状态
status = '游戏中'


def play_game():
    global score
    global food
    global status
    # 画出背景竖线
    for i in range(40):
        pygame.draw.line(screen, (147, 147, 145), (20 + i * 20, 0), (20 + i * 20, 600), 1)
    # 画出背景横线
    for i in range(30):
        pygame.draw.line(screen, (147, 147, 145), (0, i * 20), (800, i * 20), 1)

    # 贪吃蛇的移动
    if direction == 'right':
        head_x = snake_list[0][0] + 20
        head_y = snake_list[0][1]
        if [head_x, head_y] in snake_list:
            status = '结束'
        snake_list.insert(0, [head_x, head_y])
    elif direction == 'left':
        head_x = snake_list[0][0] - 20
        head_y = snake_list[0][1]
        if [head_x, head_y] in snake_list:
            status = '结束'
        snake_list.insert(0, [head_x, head_y])
    elif direction == 'up':
        head_x = snake_list[0][0]
        head_y = snake_list[0][1] - 20
        if [head_x, head_y] in snake_list:
            status = '结束'
        snake_list.insert(0, [head_x, head_y])
    elif direction == 'down':
        head_x = snake_list[0][0]
        head_y = snake_list[0][1] + 20
        if [head_x, head_y] in snake_list:
            status = '结束'
        snake_list.insert(0, [head_x, head_y])

    snake_list.pop()

    # 【画出贪吃蛇】
    for pos in snake_list:
        pygame.draw.rect(screen, (146, 172, 209), (pos[0], pos[1], 20, 20))

    # 【吃食物】
    if food == snake_list[0]:
        food = [random.randint(1, 39) * 20, random.randint(1, 29) * 20]
        snake_list.append(snake_list[-1])
        score += 1
        eat_sound.play()

    # 【画出食物】
    pygame.draw.rect(screen, (224, 205, 207), (food[0], food[1], 20, 20))


# 窗口主循环
while True:
    # 遍历事件队列
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击右上角的'X'，终止主循环
            pygame.quit()
            sys.exit()
        # 【控制方向模块】
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

    # 填充背景颜色
    screen.fill((105, 100, 123))

    # 游戏模块
    if status == '游戏中':
        play_game()

        # 游戏结束的判断机制
        if snake_list[0][0] > 800 or snake_list[0][0] < 0:
            status = '结束'
        elif snake_list[0][1] > 600 or snake_list[0][1] < 0:
            status = '结束'
    else:
        font_1 = font.render(f'你的得分是：{score}', 1, (255, 114, 86))
        screen.blit(font_1, (200, 250))

    fps = len(snake_list) + 1
    fclock.tick(fps)

    # 重绘界面
    pygame.display.update()
