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
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Project")
##

#טעינה של התמונות
cat=pygame.image.load("what i got alrady from nitzanin/images/cat.png")
tree=pygame.image.load("what i got alrady from nitzanin/images/tree.png")
TREE_SIZE = (200, WINDOW_HEIGHT)
tree=pygame.transform.scale(tree,TREE_SIZE)
cat= pygame.transform.scale(cat,CAT_SIZE)
##
#התחלת הלולאה של המשחק
running = True
while running:

    #הפעלת כפתור סגירה (חשוב שהfor יהיה בתוך הלולאה של הwhile )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        cat_x += speed_x
        cat_y += speed_y

        # Check for collision with window boundaries and reverse direction
        if cat_x <= 0 or cat_x >= WINDOW_WIDTH - 60:  # Assuming cat width is 60
            speed_x = -speed_x
        if cat_y <= 0 or cat_y >= WINDOW_HEIGHT - 60:  # Assuming cat height is 60
            speed_y = -speed_y
        screen.fill(BG_COLOR)
        screen.blit(cat, (cat_x, cat_y))
        screen.blit(tree, (200, 0))

        pygame.display.update()
        pygame.time.delay(30)




