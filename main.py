import pygame
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT

#התחלת המשחק/הפעלת הספרייה
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Project")
##

#טעינה של התמונות
cat=pygame.image.load("what i got alrady from nitzanin/images/cat.png")
tree=pygame.image.load("what i got alrady from nitzanin/images/tree.png")
##
#התחלת הלולאה של המשחק
running = True
while running:

#הפעלת כפתור סגירה (חשוב שהfor יהיה בתוך הלולאה של הwhile )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
