import pygame
import os

pygame.init()
Width, Height = 800, 500
pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hangman Game")

FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
pygame.quit()
    