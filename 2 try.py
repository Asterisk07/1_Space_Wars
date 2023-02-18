import pygame    
    
pygame.init()    
size=(400,500)
screen = pygame.display.set_mode(size)  
pygame.display.set_caption("Example program ")      
done = False    
clo=pygame.time.Clock()
while not done:    
    clo.tick(10)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:    
            done = True    
    screen.fill((1,0,0))
    pygame.draw.line(screen, (0, 255, 0), [0, 0], [50, 30], 5)
    pygame.draw.circle(screen,(120,12,200),(300,300),100)   
    # pygame.draw.ellipse(screen,(0,255,0),)
    pygame.display.flip()  