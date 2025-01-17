from json.decoder import WHITESPACE

import pygame
from constants import *

#התחלת המשחק/הפעלת הספרייה
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Project")
##

#טעינה של התמונות
cat=pygame.image.load("what i got alrady from nitzanin/images/cat.png")
tree=pygame.image.load("what i got alrady from nitzanin/images/tree.png")
screen.fill(BG_COLOR)

TREE_SIZE = (200, WINDOW_HEIGHT)
tree=pygame.transform.scale(tree,TREE_SIZE)
cat= pygame.transform.scale(cat,CAT_SIZE)
screen.blit(tree,(200,0))
screen.blit(cat,(150,300))
pygame.display.update()
##
#התחלת הלולאה של המשחק
running = True
while running:

    #הפעלת כפתור סגירה (חשוב שהfor יהיה בתוך הלולאה של הwhile )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

