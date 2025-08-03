import pygame 

pygame.init()


width = 500
height = 500
x = 200
y = 200

pygame.display.set_caption("My first pygame")
screen = pygame.display.set_mode([width, height])
fps = 60
timer = pygame.time.Clock()

run = True
while run:
    screen.fill((0, 0, 255))
    timer.tick(fps)
    player = pygame.draw.rect(screen, (255, 0, 0), (x,y, 50, 50))
    pygame.draw.circle(screen, (0, 255, 0), (250, 250), 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10  
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_DOWN:
                y += 10 
            if event.key == pygame.K_ESCAPE:
                run = False       

    pygame.display.flip()

pygame.quit()              
                                 