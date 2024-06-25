import pygame
import sys
import os
import Button
import Board
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This class represents the game state machine
class GameState:
    def __init__(self, screen, player_count):
        self.screen = screen
        self.state = 'input'
        self.player_count = player_count  # Set this to the number of players
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
        self.screen.fill((42, 165, 151))  # Change the background color
        font = pygame.font.Font('Required_Assets/AmaticSC-Bold.ttf',42)  # Use a different font
        total_text_height = self.player_count * 40  # 40 is the line height
        y = (self.screen.get_height() - total_text_height) / 2  # Start y at the vertical center
        for i, player_name in enumerate(self.player_names):
            text = font.render("PLAYER {}: {}".format(i + 1, player_name), True, (18, 64, 59))  # Change the text color
            text_rect = text.get_rect(center=(self.screen.get_width() / 2, y))  # Get the rectangle of the text and center it
            self.screen.blit(text, text_rect)
            y += 40

    def game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        Board.main(self.player_names)
        # Draw game screen

    def manager(self):
        if self.state == 'input':
            self.input()
        if self.state == 'game':
            self.game()

def main(player_count):
    Button.No_of_players = player_count
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center the window
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    game_state = GameState(screen, player_count)

    while True:
        game_state.manager()
        pygame.display.flip()
if __name__ == "__main__":
    main(Button.No_of_players)