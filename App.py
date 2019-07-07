import pygame


pygame.init()
display_height = 720
display_width = 1280
displayWindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SecondProject")
clock = pygame.time.Clock()

black = [0, 0, 0]
white = [255, 255, 255]
grey = [55, 55, 55]
running = True


def visuals():
    displayWindow.fill(white)
    pygame.display.update()
    clock.tick(30)


while running:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass
    visuals()

pygame.quit()
