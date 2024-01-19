import pygame
import math
import random
import sys

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["IDE", "REPLIT", "PYTHON", "PYGAME"]
word = random.choice(words)
guessed = []

# Add a game_over variable
game_over = False

# Add a variable to limit the number of hints
MAX_HINTS = 1
hints_used = 0

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    # Draw hint button in the top right corner
    pygame.draw.rect(win, BLACK, (WIDTH - 120, 20, 100, 50))
    text = LETTER_FONT.render("Hint", 1, WHITE)
    win.blit(text, (WIDTH - 70 - text.get_width()/2, 45 - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)


def restart_game():
    global hangman_status, guessed, game_over, word, hints_used

    hangman_status = 0
    guessed = []
    game_over = False
    hints_used = 0

    # Choose a new word for the restarted game
    word = random.choice(words)

    # Reset the visibility of each letter
    for letter in letters:
        letter[3] = True


def quit_game():
    pygame.quit()
    sys.exit()


def main():
    global hangman_status, game_over, hints_used

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
                                if hangman_status == 6:
                                    hints_used = 0  # Reset hints if the game is lost

                # Check if the hint button is clicked
                if WIDTH - 120 < m_x < WIDTH - 20 and 20 < m_y < 70 and hints_used < MAX_HINTS:
                    hint_letter = get_hint()
                    if hint_letter:
                        guessed.append(hint_letter)
                        hints_used += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You WON!")
            game_over = True
            break

        if hangman_status == 6:
            display_message("You LOST!")
            game_over = True
            break


def get_hint():
    # Get a hint by revealing a random letter from the word
    unrevealed_letters = [letter for letter in word if letter not in guessed]
    if unrevealed_letters:
        hint_letter = random.choice(unrevealed_letters)
        return hint_letter
    else:
        return None


# Add a game loop for restarting or quitting
while True:
    main()

    # Display restart and quit options after the game is over
    display_message("Do you want to play again?")
    restart_button = input("Press 'R' to restart, 'Q' to quit: ").upper()
    if restart_button == 'R':
        restart_game()
    elif restart_button == 'Q':
        quit_game()
    else:
        print("Invalid input. Please press 'R' to restart or 'Q' to quit.")
