
import pygame
import random
import os

# initlization the object
pygame.init()

# creating window
screen=pygame.display.set_mode((600,250))

# give title
pygame.display.set_caption(os.getcwd()+"My First Game..............:)")


# game spacifice variables
exit_game=False
game_over=False

# game loop
while not exit_game:
    color_change1=random.randint(0,255)   # 3* color_change use as = pixels values like color tuple (33,04,33)
    color_change2=random.randint(0,255)

    color_change3=random.randint(0,255)    

    for event in pygame.event.get():
        # print(event)
        if event.type==pygame.QUIT:
            print("Thanks for playing over game :) ")
            exit_game=True

        if event.type==pygame.KEYDOWN:   # kya any button press
            if event.key==pygame.K_q:
                exit_game=True           #quiet game when pressing q button

            if event.key==pygame.K_RIGHT:    # if user press right key
                print("yes, you press right key")

            if event.key==pygame.K_TAB:     #some press tab ; randomly change color
                screen.fill((color_change1,color_change2,color_change3))
                pygame.display.update()


pygame.quit()
quit()