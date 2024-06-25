import pygame
import Button
import players_name

pygame.font.init()

FPS = 60
WIDTH = 1200
HEIGHT = 900
BLUE = (18, 64, 59)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (42, 165, 151)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

NAME_PLATE = pygame.font.Font('Required_Assets/AmaticSC-Bold.ttf', 42)
pygame.display.set_caption("Mini Business Simulator")

def nextpage(player_count):
    players_name.main(player_count)

def draw_window():
    WIN.fill(BACKGROUND_COLOR)
    name_plate= NAME_PLATE.render("Select the number of players",True,WHITE)
    name_plate_rect = name_plate.get_rect(center=(WIDTH / 2, HEIGHT * 0.2))
    WIN.blit(name_plate, name_plate_rect)
    Button.create_button("2P",WIDTH * 0.5 - 100, HEIGHT * 0.4 - 25, 200, 50, BLUE, BLUE, lambda: nextpage(2), WIN, WHITE)
    Button.create_button("3P",WIDTH * 0.5 - 100, HEIGHT * 0.5 - 25, 200, 50, BLUE, BLUE, lambda: nextpage(3), WIN, WHITE)
    Button.create_button("4P",WIDTH * 0.5 - 100, HEIGHT * 0.6 - 25, 200, 50, BLUE, BLUE, lambda: nextpage(4), WIN, WHITE)
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