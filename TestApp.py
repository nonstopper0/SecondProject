import pygame

print("Program Starting...")
pygame.init()
display_height = 720
display_width = 1280
displayWindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

black = [0, 0, 0]
white = [255, 255, 255]
grey = [20, 20, 20]
running = True
pressed = False
finaltext = ""


def addText(event):
    global finaltext, knownchars
    text = str(event)[30]
    if pressed:
        knownchars = ["qwertyuiopasdfghjklzxcvbnm "]
        if text in str(knownchars):
            finaltext += str(text)


def text(text, color, size, x, y):
    textfont = pygame.font.SysFont("Myriad Pro", size)
    textSurf = textfont.render(text, 2, color)
    displayWindow.blit(textSurf, (x, y))


def visuals():
    global Textbox
    displayWindow.fill(grey)
    Textbox = pygame.draw.rect(displayWindow, white, pygame.Rect(200, 200, 800, 50))
    TextFont = text(finaltext, black, 40, 200, 225)
    pygame.display.update()
    clock.tick(30)
    text(finaltext, black, 20, 20, 20)


while running:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pressed:
                addText(event)
            if event.key == pygame.K_BACKSPACE:
                finaltext = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Textbox.collidepoint(mouse):
                pressed = True
            if not Textbox.collidepoint(mouse):
                pressed = False
                print(finaltext)

    visuals()


print("Program Ending...")
pygame.quit()
