import pygame




 
pygame.init()
gameWindow=pygame.display.set_mode((600,500))

pygame.display.set_caption("new world game")

# spasicifice variable
game_exit=False
game_over=False
snake_x=45
snake_y=45
snake_size=10
fps=60
sanke_valocity_x=2
sanke_valocity_y=2

#window colore
white=(255,255,255)
black=(0,0,0)


clock=pygame.time.Clock()
while not game_exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True
        if event.type==pygame.KEYDOWN: 
            if event.key==pygame.K_q:
                game_exit=True

            # snake move if down , up, left,righ key press    
            if event.key==pygame.K_DOWN:
                sanke_valocity_y+=2   # snake_y poistion 45+10
            if event.key==pygame.K_UP:
                sanke_valocity_y-=2
            
            if event.key==pygame.K_RIGHT:
                sanke_valocity_x+=2
            if event.key==pygame.K_LEFT:
                sanke_valocity_x-=2

                

    snake_x=snake_x+sanke_valocity_x
    snake_y=snake_y+sanke_valocity_y
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()