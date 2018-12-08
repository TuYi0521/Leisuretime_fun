#import modules
try :
    import pygame
    import sys
    from pygame.locals import *
    from random import randint
except :
    print("Load modules error!!")
    exit()
#define some datas
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
LOW_SPEED = 30
HIGH_SPEED = 30
LOW_SIZE = 5
HIGH_SIZE = 30
FONT_SIZE = 40
FONT_NAME = "Times"
FREQUENCE = 50
times = 0
#def random color
def randomcolor() :
    return (randint(0,255),randint(0,255),randint(0,255))
def randomspeed() :
    return randint(LOW_SPEED,HIGH_SPEED)
def randomposition() :
    return (randint(0,SCREEN_WIDTH),randint(0,SCREEN_HEIGHT))
def randomsize() :
    return randint(LOW_SIZE,HIGH_SIZE)
def randomoname() :
    return randint(0,100000)
def randomvalue() :
    return randint(0,1)#this is your own display number range
#class of sprite
class Word(pygame.sprite.Sprite) :
    def __init__(self,bornposition) :
        pygame.sprite.Sprite.__init__(self)
        self.value = randomvalue()
        self.font = pygame.font.SysFont(FONT_NAME,FONT_SIZE)
        # self.image = self.font.render(str(self.value),True,randomcolor())
        self.image = self.font.render(str(self.value), True, (0,255,0))
        self.speed = randomspeed()
        self.rect = self.image.get_rect()
        self.rect.topleft = bornposition
    def update(self) :
        self.rect = self.rect.move(0,self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
#init the available modules
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("HACKER EMPIRE CAPTION RAIN")
clock = pygame.time.Clock()
group = pygame.sprite.Group()
group_count = int(SCREEN_WIDTH / FONT_SIZE)
#mainloop
while True :
    time = clock.tick(FREQUENCE)
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            exit()
    screen.fill((0,0,0))
    for i in range(0, group_count):
        group.add(Word((i * FONT_SIZE, -FONT_SIZE)))
    group.update()
    group.draw(screen)
    pygame.display.update()