import pygame
import Button
import Player_selection
pygame.font.init()

WIDTH = 1200
HEIGHT = 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

YELLOW = (255,215,0)
ORANGE =(255,165,0)
GREEN =(0,255,0)
RED = (150,0,0)
WHITE = (255,255,255)
FPS = 60

NAME_PLATE = pygame.font.Font("Required_Assets/DancingScript-Bold.ttf", 100)

pygame.display.set_caption("Mini Business Simulator")

LOGO =pygame.transform.scale(pygame.image.load('Required_Assets/logo.png'),(WIDTH,HEIGHT))

def next_page():
    Player_selection.main()

def draw_window():
    WIN.blit(LOGO, (0, 0))
    name_plate = NAME_PLATE.render("Mini Business", True,WHITE )
    WIN.blit(name_plate,(50,50))
    name_plate = NAME_PLATE.render("Simulator", True, WHITE)
    WIN.blit(name_plate,(50,150))
    Button.create_button("Enter", 800, 600, 200, 50, RED, GREEN, next_page,WIN,WHITE)
    pygame.display.update()



def main():
    run = True
    clock=pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()


if __name__ == "__main__":
    main()
