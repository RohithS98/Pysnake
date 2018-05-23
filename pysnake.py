import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((600, 600))
done, is_blue, x, y, fx, fy, factive, size, xv, yv, le, i = False, True, 300, 300, 100, 100, True, 10, 1, 0, 3, 0
posq=[(x,y)]
clock = pygame.time.Clock()
grow, moved = False, False

def spawnfood(posq):
    while True:
        fx,fy=randint(5,55)*size,randint(5,55)*size
        if (fx,fy) not in posq:
            break
    return (fx,fy)

def drawsnake(posq,is_blue):
    screen.fill((0,0,0))
    if is_blue==True:
        for i in posq:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(i[0], i[1], size, size))
        i=posq[-1]
        pygame.draw.rect(screen, (150,150,0), pygame.Rect(i[0], i[1], size, size))
    else:
        for i in posq:
            pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), pygame.Rect(i[0], i[1], size, size))
        i=posq[-1]
        pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), pygame.Rect(i[0], i[1], size, size))

def checkhit(posq,le):
    if posq[-1] in posq[:len(posq)-1]:
        temp=posq.index(posq[-1])
        posq=posq[temp+2:]
        le=len(posq)
    return (posq,le)


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                        grow=not(grow)
        
        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and yv!=1:
            yv, xv = -1, 0
        elif (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and yv!=-1:
            yv, xv = 1, 0
        elif (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and xv!=1:
            yv, xv = 0, -1
        elif (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and xv!=-1:
            yv, xv = 0, 1
        x+=(xv*size)
        y+=(yv*size)
        if x>=600:
            x=x-600
        elif x<0:
            x=x+600
        if y>=600:
            y=y-600
        elif y<0:
            y=y+600
        posq.append((x,y))
        if len(posq)>le:
            posq=posq[1:]
        if factive==False:
            fx,fy=spawnfood(posq)
            factive=True
        if (x,y)==(fx,fy):
            factive=False
            fx, fy =-100, -100
            le+=1

        posq,le=checkhit(posq,le)
        drawsnake(posq,is_blue)
        if is_blue:
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(fx, fy, 10, 10))
        else:
            pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), pygame.Rect(fx, fy, 10, 10))
        i+=1
        if i==20:
            if grow:
                le+=1
            i=0
        
        pygame.display.flip()
        clock.tick(20)
pygame.quit()
