import pygame


pygame.init()
display_height = 720
display_width = 1280
displayWindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SecondProject")
clock = pygame.time.Clock()

running = True


def visuals():
    displayWindow.fill((0, 50, 0))
    pygame.display.update()
    clock.tick(5)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("hey")
    visuals()

pygame.quit()
