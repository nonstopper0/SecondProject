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
money = 0


class Button:
    def __init__(self, x, y, width, height, text, textsize, textcolor, boxcolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textsize = textsize
        self.textcolor = textcolor
        self.boxcolor = boxcolor

    def draw(self):
        # Create Button outline
        rectangle = pygame.draw.rect(displayWindow, self.boxcolor, pygame.Rect(self.x, self.y, self.width, self.height))
        # Create Text Object
        textfont = pygame.font.SysFont("Myriad Pro", self.textsize)
        textSurf = textfont.render(self.text, 2, self.textcolor)

        # get rect and width of text generated. Then divide by 2 to help center
        textRect = textSurf.get_rect()
        textRectWidth = textSurf.get_rect().width / 2
        textRectHeight = textSurf.get_rect().height / 2
        # move text Rect to Rectangle.Center
        textRectmove = textRect.move(rectangle.center)
        textMoveLeft = (textRectmove[0] - textRectWidth)
        textMoveUp = (textRectmove[1] - textRectHeight)
        # create new text rect object using subtracted numbers
        textNew = (textMoveLeft, textMoveUp, textRectmove[2], textRectmove[3])
        # display text to screen
        displayWindow.blit(textSurf, textNew)
        # return rectangle rect for an easier collide method using collidepoint()
        return rectangle


MoneyButton = Button(500, 500, 200, 200, "MONEY", 40, white, black)
MoneyDisplay = Button(10, 10, 50, 50, str(money), 40, white, black)


def visuals():
    global MoneyB, MoneyD
    displayWindow.fill(white)
    MoneyB = MoneyButton.draw()
    MoneyD = MoneyDisplay.draw()
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
            if MoneyB.collidepoint(mouse):
                money += 1
                print(money)

    visuals()

print("Program Ending...")
pygame.quit()
