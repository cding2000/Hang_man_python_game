import pygame
import math

pygame.init()
Width, Height = 800, 500
win = pygame.display.set_mode((Width, Height))
pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hangman Game")

Radius = 20
Gap = 15
A = 65
startx = round((Width - (Radius * 2 + Gap) * 13) / 2) 
starty = 400
letters = []
for i in range(26):
    x = startx + Gap * 2 + ((Radius * 2 + Gap) * (i % 13))
    y = starty + ((i // 13) * (Gap + Radius * 2))
    letters.append([x, y, chr(A + i), True])
    
Letter_Font = pygame.font.SysFont('comicsans', 30)


images =[]
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

hangman_status = 0

white = (255, 255, 255)
black = (0, 0 ,0)

FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill((255, 255, 255))
    
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, black, (x, y), Radius, 3)
            text = Letter_Font.render(ltr, 1, black)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        
        
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()
    
    
while run:
    clock.tick(FPS)
    
    draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < Radius:
                        letter[3] = False
pygame.quit()
    