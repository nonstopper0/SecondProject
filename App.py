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
ball1Locationx = 0
ball1Locationy = 0
running = True


def visuals():
    global ball1
    displayWindow.fill(white)
    ball1 = pygame.draw.circle(displayWindow, black, (ball1Locationx, ball1Locationy), 40, 3)
    pygame.display.update()
    clock.tick(30)


while running:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ball1Locationy += 20
                print("hey")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ball1.collidepoint(mouse):
                print("ya")
    visuals()

pygame.quit()
