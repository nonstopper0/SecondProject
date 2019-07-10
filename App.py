import pygame

print("Program Starting...")
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


class Button:
    def __init__(self, x, y, width, height, text, textSize, textcolor, boxcolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textSize = textSize
        self.textcolor = textcolor
        self.boxcolor = boxcolor

    def draw(self):
        # Create Button outline
        rectangle = pygame.draw.rect(displayWindow, self.boxcolor, pygame.Rect(self.x, self.y, self.width, self.height))
        # Create Text Object
        textfont = pygame.font.SysFont("Myriad Pro", self.textSize)
        textSurf = textfont.render(self.text, 2, self.textcolor)

        # get rect and width of text generated. Then divide by 2 to help center
        textRect, textRectSub = textSurf.get_rect(),textSurf.get_rect().width / 2
        textRectmove = textRect.move(rectangle.center)
        textFinal = (textRectmove[0] - textRectSub)
        textNew = (textFinal, textRectmove[1], textRectmove[2], textRectmove[3])

        print(textNew)

        displayWindow.blit(textSurf, textNew)

        return rectangle


PlayButton = Button(500, 500, 200, 200, "Hey now", 30, grey, black)


def visuals():
    global Test
    displayWindow.fill(white)
    Test = PlayButton.draw()
    pygame.display.update()
    clock.tick(30)


while running:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Test.collidepoint(mouse):
                print("hey")
    visuals()

print("Program Ending...")
pygame.quit()
