from random  import *
import pygame
from constants import *
cat_x = randint(0, WINDOW_WIDTH - 60)
cat_y = randint(0, WINDOW_HEIGHT - 60)
score=0
speed_x = 5
speed_y = 3
#התחלת המשחק/הפעלת הספרייה
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Project")
##

#טעינה של התמונות
cat=pygame.image.load("what i got alrady from nitzanin/images/cat.png")
tree=pygame.image.load("what i got alrady from nitzanin/images/tree.png")
TREE_SIZE = (200, WINDOW_HEIGHT)
tree=pygame.transform.scale(tree,TREE_SIZE)
cat= pygame.transform.scale(cat,CAT_SIZE)
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
##
#התחלת הלולאה של המשחק
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cat_rect = cat.get_rect(topleft=(cat_x, cat_y))  # Remove the offset
            if cat_rect.collidepoint(event.pos):
                score += 1
                print(f"Score: {score}")
    cat_x += speed_x
    cat_y += speed_y
    if cat_x <= 0 or cat_x >= WINDOW_WIDTH - CAT_SIZE[0]:
        speed_x = -speed_x
    if cat_y <= 0 or cat_y >= WINDOW_HEIGHT - CAT_SIZE[1]:
        speed_y = -speed_y
    screen.fill(BG_COLOR)
    screen.blit(tree, (200, 0))
    screen.blit(cat, (cat_x, cat_y))
    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color for the text
    screen.blit(score_text, SCORE_POS)
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()
