import pygame
import sys
import Button
No_of_players = Button.No_of_players
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This class represents the game state machine
class GameState:
    def __init__(self,No_of_players):
        self.state = 'input'
        self.player_count = No_of_players  # Set this to the number of players
        self.player_names = ['' for _ in range(self.player_count)]
        self.current_player = 0

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if self.state == 'input':
                        self.player_names[self.current_player] = self.player_names[self.current_player][:-1]
                elif event.key == pygame.K_RETURN:
                    if self.current_player < self.player_count - 1:
                        self.current_player += 1
                    else:
                        self.state = 'game'
                else:
                    if self.state == 'input':
                        self.player_names[self.current_player] += event.unicode
        screen.fill((42, 165, 151))  # Change the background color
        Button.create_button("Enter",800,600,200,50,(255,0,0),(0,255,0),next_page,screen,(255,255,255))
        font = pygame.font.Font('AmaticSC-Bold.ttf',42)  # Use a different font
        total_text_height = self.player_count * 40  # 40 is the line height
        y = (screen.get_height() - total_text_height) / 2  # Start y at the vertical center
        for i, player_name in enumerate(self.player_names):
            text = font.render("PLAYER {}: {}".format(i + 1, player_name), True, (18, 64, 59))  # Change the text color
            text_rect = text.get_rect(center=(screen.get_width() / 2, y))  # Get the rectangle of the text and center it
            screen.blit(text, text_rect)
            y += 40

    def game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Jai shri ram")
        # Draw game screen

    def manager(self):
        if self.state == 'input':
            self.input()
        if self.state == 'game':
            self.game()
def next_page(self):
    print("Jai shri ram") 
pygame.init()
screen = pygame.display.set_mode((800, 600))
game_state = GameState(No_of_players)

while True:
    game_state.manager()
    pygame.display.flip()