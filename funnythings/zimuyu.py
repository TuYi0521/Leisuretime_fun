try:
    import pygame
    from sys import exit
    from pygame.locals import *
    import random
    import time
except:
    print("Load modules error!!")
    exit()

# init the available modules
pygame.init()
SCREEN_SIZE = (640, 640)
pygame.display.set_caption("HACKER EMPIRE CAPTION RAIN")
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
# event_text = []
texts = [['0'] * 80]

while True:
    event = pygame.event.poll()

    if event.type == QUIT:
        pygame.quit()
        exit()

    i = 0
    t = 80
    tx = []
    while i < t:
        tx.append(chr(random.randint(1, 127)))
        i += 1
    texts.append(tx)
    texts = texts[int(-SCREEN_SIZE[1] / font_height):]
    # 这个切片操作保证了event_text里面只保留一个屏幕的文字



    screen.fill((0, 0, 0))  # 屏幕填充黑色
    # 找一个合适的起笔位置，最下面开始但是要留一行的空
    y = SCREEN_SIZE[1] - font_height

    for text in texts:
        x = 0
        for c in text:
            screen.blit(font.render(c, True, (0, 255, 0)), (x, y))
            x += 20
            # 以后会讲
        y -= font_height
        # 把笔提一行
        i = i + 1
        
        time.sleep(0.0001)

    pygame.display.update()
    # pygame.image.save(screen, "zimuyu.png")
