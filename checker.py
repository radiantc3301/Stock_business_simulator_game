import pygame
pygame.font.init()
import Player_selection
import Button
import random

WIDTH = 1200
HEIGHT = 900
FPS = 60
FONT1 = pygame.font.Font("Required_Assets/LobsterTwo-Italic.ttf", 30)
FONT2 = pygame.font.Font(None, 30)
JAIL = pygame.transform.scale(pygame.image.load('Required_Assets/JAIL.jpg'),(72,72))
START = pygame.transform.scale(pygame.image.load('Required_Assets/START.jpg'),(72,72))
CHANCE = pygame.transform.scale(pygame.image.load('Required_Assets/CHANCE.jpg'),(72,72))
COMMUNITY_CHEST = pygame.transform.scale(pygame.image.load('Required_Assets/CHEST.jpg'),(72,72))
WINDFALL_DAY =pygame.transform.scale(pygame.image.load('Required_Assets/Windfall_day.jpg'),(72,72))
MARKET_CLOSED = pygame.transform.scale(pygame.image.load('Required_Assets/Market_close.jpg'),(72,72))
Player_1 = pygame.transform.scale(pygame.image.load('Required_Assets/yellow_token.jpg'),(30,30))
Player_2 = pygame.transform.scale(pygame.image.load('Required_Assets/blue_token.jpg'),(30,30))
Player_3 = pygame.transform.scale(pygame.image.load('Required_Assets/green_token.jpg'),(30,30))
Player_4 = pygame.transform.scale(pygame.image.load('Required_Assets/red_token.jpg'),(30,30))
BANK = pygame.transform.scale(pygame.image.load('Required_Assets/bank.png'), (240, 180))
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
DICE_IMAGES = [pygame.transform.scale(pygame.image.load(f'Required_Assets/{i}.png'), (50, 50)) for i in range(1, 7)]

# Define the roll dice button
ROLL_DICE_BUTTON = pygame.Rect(50, HEIGHT // 2 - 75, 150, 50)

# Define the current dice image
current_dice_value = 1
current_dice_image = DICE_IMAGES[0]

def draw_lines(surface,colour):

    # Outer square
    pygame.draw.line(surface,colour,(300,150),(900,150),3)
    pygame.draw.line(surface,colour,(300,150),(300,750),3)
    pygame.draw.line(surface,colour,(300,750),(900,750),3)
    pygame.draw.line(surface,colour,(900,150),(900,750),3)
    # Inner square
    pygame.draw.line(surface,colour,(375,675),(825,675),3)
    pygame.draw.line(surface,colour,(375,675),(375,225),3)
    pygame.draw.line(surface,colour,(375,225),(825,225),3)
    pygame.draw.line(surface,colour,(825,225),(825,675),3)
    # Start button
    pygame.draw.line(surface,colour,(825,675),(900,675),3)
    pygame.draw.line(surface,colour,(825,675),(825,750),3)
    WIN.blit(START,(828,678))
    # Token 1
    pygame.draw.line(surface,colour,(750,675),(750,750),3)
    # Token 2
    pygame.draw.line(surface,colour,(675,675),(675,750),3)
    # Token 3
    pygame.draw.line(surface,colour,(600,675),(600,750),3)
    # Token 4
    pygame.draw.line(surface,colour,(525,675),(525,750),3)
    # Chance
    WIN.blit(CHANCE,(528,678))
    # Token 5
    pygame.draw.line(surface,colour,(450,675),(450,750),3)
    # Token 6
    pygame.draw.line(surface,colour,(375,675),(375,750),3)
    # Token 7
    pygame.draw.line(surface,colour,(375,675),(300,675),3)
    # JAIL
    WIN.blit(JAIL,(303,678))
    # Token 8
    pygame.draw.line(surface,colour,(375,600),(300,600),3)
    # Token 9
    pygame.draw.line(surface,colour,(375,525),(300,525),3)
    # Token 10
    pygame.draw.line(surface,colour,(375,450),(300,450),3)
    # Community Chest
    WIN.blit(COMMUNITY_CHEST,(303,453))
    # Token 11
    pygame.draw.line(surface,colour,(375,375),(300,375),3)
    # Token 12
    pygame.draw.line(surface,colour,(375,300),(300,300),3)
    # Token 13
    pygame.draw.line(surface,colour,(375,225),(300,225),3)
    # Chance
    WIN.blit(WINDFALL_DAY,(303,153))
    # Token 14
    pygame.draw.line(surface,colour,(375,225),(375,150),3)
    # Token 15
    pygame.draw.line(surface,colour,(450,225),(450,150),3)
    # Token 16
    pygame.draw.line(surface,colour,(525,225),(525,150),3)
    # Token 17
    pygame.draw.line(surface,colour,(600,225),(600,150),3)
    # Token 18
    pygame.draw.line(surface,colour,(675,225),(675,150),3)
    # Community Chest
    WIN.blit(COMMUNITY_CHEST,(678,153))
    # Token 19
    pygame.draw.line(surface,colour,(750,225),(750,150),3)
    # Token 20
    pygame.draw.line(surface,colour,(825,225),(825,150),3)
    WIN.blit(MARKET_CLOSED,(828,153))
    # Token 21
    pygame.draw.line(surface,colour,(825,225),(900,225),3)
    # Token 22
    pygame.draw.line(surface,colour,(825,300),(900,300),3)
    # Token 23
    pygame.draw.line(surface,colour,(825,375),(900,375),3)
    # Chance
    WIN.blit(CHANCE,(828,378))
    # Token 24
    pygame.draw.line(surface,colour,(825,450),(900,450),3)
    # Token 25
    pygame.draw.line(surface,colour,(825,525),(900,525),3)
    # Token 26
    pygame.draw.line(surface,colour,(825,600),(900,600),3)
    # Token 27
    pygame.draw.line(surface,colour,(825,675),(900,675),3)

    font = pygame.font.Font(None, 25)

    # Your existing code to draw the lines goes here...

    # Positions where the stock names should be rendered.
    
    # Render the stock names.
    font = pygame.font.Font(None, 22)  # Change 50 to the size you want.

    
    # Update the display.
def exit_page():
    pygame.quit() 
def restart_page():
    Player_selection.main()


def draw_window():
    WIN.fill((0, 0, 255))
    Board = pygame.Rect((300, 150, 600, 600))
    pygame.draw.rect(WIN, (200, 255, 200), Board)
    Board = pygame.Rect((375, 225, 450, 450))
    pygame.draw.rect(WIN, (255, 255, 255), Board)

    # Draw the images
    WIN.blit(START, (828, 678))
    WIN.blit(CHANCE, (528, 678))
    WIN.blit(COMMUNITY_CHEST, (303, 453))
    WIN.blit(WINDFALL_DAY, (303, 153))
    WIN.blit(MARKET_CLOSED, (828, 153))

    draw_lines(WIN, (0, 0, 0))

    pygame.draw.rect(WIN, (0, 255, 0), ROLL_DICE_BUTTON)  # Draw the button
    WIN.blit(FONT1.render('Roll Dice', True, (0, 0, 0)), (ROLL_DICE_BUTTON.x + 20, ROLL_DICE_BUTTON.y + 10))  # Draw the button text
    WIN.blit(current_dice_image, (100, HEIGHT // 2))  # Draw the dice image

    # Add the new text
    title_font = pygame.font.Font(None, 50)  # Create a new font object for the title
    title_font.set_underline(True)  # Set the font to be underlined
    title_text = title_font.render('BUSINESS GAME', True, (0, 0, 255))
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Position the title in the center of the board
    WIN.blit(title_text, title_rect)

    WIN.blit(BANK, (WIDTH - 620, 230))
    
    # Chance
    chance_font = pygame.font.Font(None, 30)  # Create a new font object for the chance text
    chance_heading = chance_font.render('CHANCE', True, (255, 0, 0))
    chance_heading_rect = chance_heading.get_rect(center=(WIDTH // 4 + 190, 250))  # Position the chance heading at the top left
    WIN.blit(chance_heading, chance_heading_rect)
    bullet_points = ["", "", "", "", "", ""]  # Empty bullet points
    for i, point in enumerate(bullet_points):
        WIN.blit(chance_font.render(f"{i + 1}. {point}", True, (0, 0, 0)), (WIDTH // 4 + 90, 270 + i * 25))  # Position the bullet points

    # Rules
    rules_font = pygame.font.Font(None, 30)  # Create a new font object for the rules title
    rules_title = rules_font.render('RULES', True, (255, 0, 0))  # Create a surface with the rules title
    WIN.blit(rules_title, (450, HEIGHT - 420))  # Draw the rules title at the bottom left

    rules = ["", "", "", "", "", ""]  # Empty rules
    for i, rule in enumerate(rules):
        WIN.blit(rules_font.render(f"{i + 1}. {rule}", True, (0, 0, 0)), (390, HEIGHT - 385 + i * 25))  # Draw the rules

    # Community Chest
    community_font = pygame.font.Font(None, 30)  # Create a new font object for the community chest text
    community_heading = community_font.render('COMMUNITY CHEST', True, (255, 0, 0))
    community_heading_rect = community_heading.get_rect(center=(3 * WIDTH // 4 - 190, HEIGHT - 410))  # Position the community chest heading at the bottom right
    WIN.blit(community_heading, community_heading_rect)
    bullet_points = ["", "", "", "", "", ""]  # Empty bullet points
    for i, point in enumerate(bullet_points):
        WIN.blit(community_font.render(f"{i + 1}. {point}", True, (0, 0, 0)), (3 * WIDTH // 4 - 305, HEIGHT - 380 + i * 25))  # Position the bullet points

    Button.create_button("RESTART", 650, 800, 150, 50, (0, 255, 0), (0, 0, 0), restart_page, WIN, (255, 255, 255))
    Button.create_button("EXIT", 400, 800, 150, 50, (255, 0, 0), (0, 0, 0), exit_page, WIN, (255, 255, 255))
    # pygame.draw.rect(WIN,(150,150,255),(500,425,167,50))
    # name_plate = FONT1.render("Business game",True,(0,0,0))
    # WIN.blit(name_plate,(500,425))
    # pygame.draw.rect(WIN,(150,150,255),(700,275,70,30))
    # name_plate = FONT2.render("BANK",True,(0,0,0))
    # WIN.blit(name_plate,(705,280))
    # pygame.draw.line(WIN, (255, 0, 0), (100, 100), (200, 200), 5)
    pygame.display.update()


def roll_dice():
    global current_dice_image, current_dice_value
    current_dice_value = random.randint(1, 6)
    current_dice_image = DICE_IMAGES[current_dice_value - 1]
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if ROLL_DICE_BUTTON.collidepoint(x, y):
                    roll_dice()
        draw_window()

if __name__ == "_main_":
    main()