import pygame
pygame.font.init()
import Game_login
import random
import Button
import Tokens
WIDTH = 1200
HEIGHT = 900
FPS = 60
Total_no_of_moves = 2
Token_list = Tokens.Token_list
FONT1 = pygame.font.Font("Required_Assets/LobsterTwo-Italic.ttf", 30)
FONT2 = pygame.font.Font(None, 50)
PURSE_FONT = pygame.font.Font(None, 50)
WINNER_FONT = pygame.font.Font(None, 70)
WHITE = (255,255,255)
MARKET_CRASH = pygame.transform.scale(pygame.image.load('Required_Assets/Market_crash.png'),(72,72))
BANK = pygame.image.load('Required_Assets/bank.png')
BANK = pygame.transform.scale(BANK, (220, 180))
START = pygame.transform.scale(pygame.image.load('Required_Assets/START.png'),(72,72))
CHANCE = pygame.transform.scale(pygame.image.load('Required_Assets/CHANCE.png'),(72,72))
COMMUNITY_CHEST = pygame.transform.scale(pygame.image.load('Required_Assets/CHEST.png'),(72,72))
WINDFALL_DAY =pygame.transform.scale(pygame.image.load('Required_Assets/Windfall_day.png'),(72,72))
MARKET_CLOSED = pygame.transform.scale(pygame.image.load('Required_Assets/Market_close.png'),(75,75))
Player_1 = pygame.transform.scale(pygame.image.load('Required_Assets/yellow_token.png'),(40,40))
Player_2 = pygame.transform.scale(pygame.image.load('Required_Assets/blue_token.png'),(40,40))
Player_3 = pygame.transform.scale(pygame.image.load('Required_Assets/green_token.png'),(40,40))
Player_4 = pygame.transform.scale(pygame.image.load('Required_Assets/red_token.png'),(40,40))
stocks = ["Wipro", "HDFC", "Adani", "ONGC", "Infosys", "L&T", "ITC", "SBI", "NTPC", "HCL", "Kotak", "Nestle", "Britannia", "Apollo", "Bajaj", "ICICI", "Mahindra", "Airtel", "Eicher", "Titan"]
price = [100, 195, 250, 40, 150, 285, 90, 160, 60, 180, 205, 230, 320, 345, 360, 120, 215, 140, 300, 270]
positions1 = [(752+8, 677+8+2), (677+8, 677+8+2), (602+8, 677+8+2), (452+8, 677+8+2), (377+8, 677+8+2), (302+8, 602+8), (302+8, 527+8), (302+8, 377+8), (302+8, 302+8), (302+8, 227+8), (377+8, 152+8), (452+8, 152+8), (527+8, 152+8), (602+8, 152+8), (752+8, 152+8), (827+10, 227+8),(827+10,302+8),(827+10,452+8),(827+10,527+8),(827+10,602+8),(827+10,677+8)]
positions2 = [(752+8, 732-12), (677+8, 732-12), (602+8, 732-12), (452+8, 732-12), (377+8, 732-12), (302+8, 657-12), (302+8, 582-12), (302+8, 432-12), (302+8, 357-12), (302+8, 282-12), (377+8, 207-12), (452+8, 207-12), (527+8, 207-12), (602+8, 207-12), (752+8, 207-12), (827+10, 282-12),(827+10,357-12),(827+10,507-12),(827+10,582-12),(827+10,657-12),(827+10,732-12)]
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
class Player:
    def __init__(self,Player_no,Player_Amount,Player_name):
        self.Player_no = Player_no
        self.Player_Amount = Player_Amount
        self.Player_name = Player_name
    def get_player_no(self):
        return self.Player_no
    def get_player_amount(self):
        return self.Player_Amount
    def get_player_name(self):
        return self.Player_name
    def update_player_amount(self,amount):
        self.Player_Amount = amount
Player_1_details = Player(0,1200,Button.Player_1)
Player_2_details = Player(1,1200,Button.Player_2)
Player_3_details = Player(2,1200,Button.Player_3)
Player_4_details = Player(3,1200,Button.Player_4)
Player_identities = [Player_1_details,Player_2_details,Player_3_details,Player_4_details]
Player1_coordinates = {(825,675):Token_list[0],(750,675):Token_list[1],(675,675):Token_list[2],(600,675):Token_list[3],(525,675):Token_list[4],(450,675):Token_list[5],(375,675):Token_list[6],(300,675):Token_list[7],(300,600):Token_list[8],(300,525):Token_list[9],(300,450):Token_list[10],(300,375):Token_list[11],(300,300):Token_list[12],(300,225):Token_list[13],(300,150):Token_list[14],(375,150):Token_list[15],(450,150):Token_list[16],(525,150):Token_list[17],(600,150):Token_list[18],(675,150):Token_list[19],(750,150):Token_list[20],(825,150):Token_list[21],(825,225):Token_list[22],(825,300):Token_list[23],(825,375):Token_list[24],(825,450):Token_list[25],(825,525):Token_list[26],(825,600):Token_list[27]}
Player2_coordinates = {(865,675):Token_list[0],(790,675):Token_list[1],(715,675):Token_list[2],(640,675):Token_list[3],(565,675):Token_list[4],(490,675):Token_list[5],(415,675):Token_list[6],(340,675):Token_list[7],(340,600):Token_list[8],(340,525):Token_list[9],(340,450):Token_list[10],(340,375):Token_list[11],(340,300):Token_list[12],(340,225):Token_list[13],(340,150):Token_list[14],(415,150):Token_list[15],(490,150):Token_list[16],(565,150):Token_list[17],(640,150):Token_list[18],(715,150):Token_list[19],(790,150):Token_list[20],(865,150):Token_list[21],(865,225):Token_list[22],(865,300):Token_list[23],(865,375):Token_list[24],(865,450):Token_list[25],(865,525):Token_list[26],(865,600):Token_list[27]}
Player3_coordinates = {(825,715):Token_list[0],(750,715):Token_list[1],(675,715):Token_list[2],(600,715):Token_list[3],(525,715):Token_list[4],(450,715):Token_list[5],(375,715):Token_list[6],(300,715):Token_list[7],(300,640):Token_list[8],(300,565):Token_list[9],(300,490):Token_list[10],(300,415):Token_list[11],(300,340):Token_list[12],(300,265):Token_list[13],(300,190):Token_list[14],(375,190):Token_list[15],(450,190):Token_list[16],(525,190):Token_list[17],(600,190):Token_list[18],(675,190):Token_list[19],(750,190):Token_list[20],(825,190):Token_list[21],(825,265):Token_list[22],(825,340):Token_list[23],(825,415):Token_list[24],(825,490):Token_list[25],(825,565):Token_list[26],(825,640):Token_list[27]}
Player4_coordinates = {(865,715):Token_list[0],(790,715):Token_list[1],(715,715):Token_list[2],(640,715):Token_list[3],(565,715):Token_list[4],(490,715):Token_list[5],(415,715):Token_list[6],(340,715):Token_list[7],(340,640):Token_list[8],(340,565):Token_list[9],(340,490):Token_list[10],(340,415):Token_list[11],(340,340):Token_list[12],(340,265):Token_list[13],(340,190):Token_list[14],(415,190):Token_list[15],(490,190):Token_list[16],(565,190):Token_list[17],(640,190):Token_list[18],(715,190):Token_list[19],(790,190):Token_list[20],(865,190):Token_list[21],(865,265):Token_list[22],(865,340):Token_list[23],(865,415):Token_list[24],(865,490):Token_list[25],(865,565):Token_list[26],(865,640):Token_list[27]}
Player_coordinate_assets=[Player1_coordinates,Player2_coordinates,Player3_coordinates,Player4_coordinates]
Player_Coordinates = [list(Player1_coordinates.keys()),list(Player2_coordinates.keys()),list(Player3_coordinates.keys()),list(Player4_coordinates.keys())]
Player_1_rectangle = pygame.Rect(825,675,40,40)
Player_2_rectangle = pygame.Rect(865,675,40,40)
Player_3_rectangle = pygame.Rect(825,715,40,40)
Player_4_rectangle = pygame.Rect(865,715,40,40)
Player_rectangles = [Player_1_rectangle,Player_2_rectangle,Player_3_rectangle,Player_4_rectangle]
DICE_IMAGES = [pygame.transform.scale(pygame.image.load(f'Required_Assets/{i}.png'), (50, 50)) for i in range(1, 7)]
# global current_dice_image, current_dice_value

# Define the roll dice button
ROLL_DICE_BUTTON = pygame.Rect(50, HEIGHT // 2 - 75, 150, 50)
BUY = pygame.Rect(125,800,150,50)
IGNORE = pygame.Rect(925,800,150,50)
# Define the current dice image
current_dice_value = 1
current_dice_image = DICE_IMAGES[0]

def draw_rectangles(Token_list):
    for i in range(len(Token_list)):
        if(Token_list[i].get_special_status() == 0):
            pygame.draw.rect(WIN,Token_list[i].get_colour(),(Token_list[i].get_x_coordinates(),Token_list[i].get_y_coordinates(),Token_list[i].get_width(),Token_list[i].get_height()))

def draw_lines(surface,colour,):
    # Other coloumns
    WIN.blit(START,(828,678))
    WIN.blit(COMMUNITY_CHEST,(528,678))
    WIN.blit(MARKET_CRASH,(303,678))
    WIN.blit(COMMUNITY_CHEST,(303,453))
    WIN.blit(WINDFALL_DAY,(303,153))
    WIN.blit(COMMUNITY_CHEST,(678,153))
    WIN.blit(MARKET_CLOSED,(828,153))
    WIN.blit(COMMUNITY_CHEST,(828,378))
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
    # Token 1
    pygame.draw.line(surface,colour,(750,675),(750,750),3)
    # Token 2
    pygame.draw.line(surface,colour,(675,675),(675,750),3)
    # Token 3
    pygame.draw.line(surface,colour,(600,675),(600,750),3)
    # Token 4
    pygame.draw.line(surface,colour,(525,675),(525,750),3)
    # Token 5
    pygame.draw.line(surface,colour,(450,675),(450,750),3)
    # Token 6
    pygame.draw.line(surface,colour,(375,675),(375,750),3)
    # Token 7
    pygame.draw.line(surface,colour,(375,675),(300,675),3)
    # Token 8
    pygame.draw.line(surface,colour,(375,600),(300,600),3)
    # Token 9
    pygame.draw.line(surface,colour,(375,525),(300,525),3)
    # Token 10
    pygame.draw.line(surface,colour,(375,450),(300,450),3)
    # Token 11
    pygame.draw.line(surface,colour,(375,375),(300,375),3)
    # Token 12
    pygame.draw.line(surface,colour,(375,300),(300,300),3)
    # Token 13
    pygame.draw.line(surface,colour,(375,225),(300,225),3)
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
    # Token 19
    pygame.draw.line(surface,colour,(750,225),(750,150),3)
    # Token 20
    pygame.draw.line(surface,colour,(825,225),(825,150),3)
    # Token 21
    pygame.draw.line(surface,colour,(825,225),(900,225),3)
    # Token 22
    pygame.draw.line(surface,colour,(825,300),(900,300),3)
    # Token 23
    pygame.draw.line(surface,colour,(825,375),(900,375),3)
    # Token 24
    pygame.draw.line(surface,colour,(825,450),(900,450),3)
    # Token 25
    pygame.draw.line(surface,colour,(825,525),(900,525),3)
    # Token 26
    pygame.draw.line(surface,colour,(825,600),(900,600),3)
    # Token 27
    pygame.draw.line(surface,colour,(825,675),(900,675),3)
    # Tokenship lines:
    pygame.draw.line(surface,colour,(375,215),(675,215),3)
    pygame.draw.line(surface,colour,(750,215),(825,215),3)
    pygame.draw.line(surface,colour,(365,225),(365,450),3)
    pygame.draw.line(surface,colour,(365,525),(365,675),3)
    pygame.draw.line(surface,colour,(375,685),(525,685),3)
    pygame.draw.line(surface,colour,(600,685),(825,685),3)
    pygame.draw.line(surface,colour,(835,225),(835,375),3)
    pygame.draw.line(surface,colour,(835,450),(835,675),3)

    for i in range(len(stocks)):
        text_surface = pygame.font.Font(None,20).render(stocks[i], True, (0, 0, 0))  # Change the color as needed.
        surface.blit(text_surface, positions1[i])
    
    for i in range(len(price)):
        text_surface = pygame.font.Font(None,20).render(str(price[i]), True, (0, 0, 0))
        surface.blit(text_surface, positions2[i])

def exit_page():
    pygame.quit() 

def wrap_text(text, font, max_width):
    words = text.split(' ')
    wrapped_text = ''
    line = ''
    for word in words:
        if font.size(line + ' ' + word)[0] <= max_width:
            line += (' ' if line else '') + word
        else:
            wrapped_text += line + '\n'
            line = word
    wrapped_text += line
    return wrapped_text

def draw_window(player_rectangle,purse,self):
    WIN.fill((0,0,255))
    Board = pygame.Rect((300,150,600,600))
    pygame.draw.rect(WIN,(200,255,200),Board)
    Board = pygame.Rect((375,225,450,450))
    pygame.draw.rect(WIN,(255,255,255),Board)
    title_font = pygame.font.Font(None, 50)  # Create a new font object for the title
    title_text = title_font.render('BUSINESS GAME', True, (0, 0, 255))
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 15))  # Position the title in the center of the board
    WIN.blit(title_text, title_rect)

    WIN.blit(BANK, (380, 230))
    # Rules
    rule_font = pygame.font.Font(None, 22)
    rules_font = pygame.font.Font(None, 18)  # Create a new font object for the rules title
    rules_title = rule_font.render('RULES', True, (255, 0, 0))  # Create a surface with the rules title
    WIN.blit(rules_title, (565, HEIGHT - 445))  # Draw the rules title at the bottom left

    rules = ["1. If you land on a stock that is not owned by anyone, then you can choose to buy it or ignore.", "2. If you land on a stock that is owned by someone then you have pay a dividend of 15%.", "3. The outome of community chest is determined by your last dice value", "4. The game is completed when either a total of 250 moves have been player or someone ends with a negative balance. In either case the player with most amount of money left will win.","5. Going through start gives you 50$, Windfall day gives you 150$, Market-crash makes you lose 150$ and in market close nothing happens","6. If you have less than 150$ then you have high risk for bankruptcy as an unlucky chance or market crash can lower your balance to negative.","7. At the end of the game stocks of all the players would be squared off and the player(s) with the greatest amount of money will win the game."]
    line_y = HEIGHT - 430
    for rule in rules:
        wrapped_text = wrap_text(rule, rules_font, 435)  # Adjust max_width as needed
        lines = wrapped_text.split('\n')
        for line in lines:
            WIN.blit(rules_font.render(line, True, (0, 0, 0)), (390, line_y))
            line_y += 14

    # Community Chest
    community_font = pygame.font.Font(None, 22)  # Create a new font object for the community chest text
    community_heading = community_font.render('COMMUNITY CHEST', True, (255, 0, 0))
    community_heading_rect = community_heading.get_rect(center=(3 * WIDTH // 4 - 190, HEIGHT - 650))  # Position the community chest heading at the bottom right
    WIN.blit(community_heading, community_heading_rect)
    bullet_points = ["Go to market crash day", "Go to windfall-day", "get a check of 50$", "Late tax fee, 75$", "Go to market close", "Get a bonus of 25$"]  # Empty bullet points
    for i, point in enumerate(bullet_points):
        WIN.blit(community_font.render(f"{i + 1}. {point}", True, (0, 0, 0)), (3 * WIDTH // 4 - 280, HEIGHT - 630 + i * 25))  # Position the bullet points

    draw_lines(WIN,(0,0,0))
    draw_rectangles(Token_list)
    pygame.draw.rect(WIN, (0, 255, 0), ROLL_DICE_BUTTON)  # Draw the button
    pygame.draw.rect(WIN,(255,0,0),BUY)
    pygame.draw.rect(WIN,(0,255,0),IGNORE)
    player_2 = PURSE_FONT.render(self[1]+": "+str(purse[1]), True, WHITE)
    WIN.blit(PURSE_FONT.render(self[0]+": "+str(purse[0]), True, WHITE),(10,10))
    WIN.blit(player_2,(WIDTH-player_2.get_width()-10,10))
    if(len(purse)>2):
        player_3 = PURSE_FONT.render(self[2]+": "+str(purse[2]), True, WHITE)
        WIN.blit(player_3,(10,200))
    if(len(purse)>3):
        player_4 = PURSE_FONT.render(self[3]+": "+str(purse[3]), True, WHITE)
        WIN.blit(player_4,(WIDTH-player_4.get_width()-10,200))
    WIN.blit(FONT1.render('Roll Dice', True, (0, 0, 0)), (ROLL_DICE_BUTTON.x + 20, ROLL_DICE_BUTTON.y + 10))  # Draw the button text
    WIN.blit(current_dice_image, (100, HEIGHT // 2))  # Draw the dice image
    WIN.blit(FONT2.render("BUY",True,(255,255,255)),(BUY.x + 40,BUY.y+10))
    WIN.blit(FONT2.render("IGNORE",True,(255,255,255)),(IGNORE.x + 5,IGNORE.y+10))
    Button.create_button("EXIT",525,800,150,50,(255,0,0),(0,0,0),exit_page,WIN,(255,255,255))
    WIN.blit(Player_1,(player_rectangle[0].x,player_rectangle[0].y))
    WIN.blit(Player_2,(player_rectangle[1].x,player_rectangle[1].y))
    if(Button.No_of_players>2):
        WIN.blit(Player_3,(player_rectangle[2].x,player_rectangle[2].y))
    if(Button.No_of_players>3):
        WIN.blit(Player_4,(player_rectangle[3].x,player_rectangle[3].y))
    pygame.display.update()

def roll_dice():
    global current_dice_image, current_dice_value
    current_dice_value = random.randint(1, 6)
    current_dice_image = DICE_IMAGES[current_dice_value - 1]
    pygame.display.update()

def Player_movement(Player,Player_no,Player_coordinates,Dice_move):
    if(Player_no >= Button.No_of_players):
        Player_no = Player_no - Button.No_of_players
    if Player_coordinates[Player_no].index((Player[Player_no].x,Player[Player_no].y))+Dice_move>27:
        index = (Player_coordinates[Player_no].index((Player[Player_no].x,Player[Player_no].y))+Dice_move)%28
        Player[Player_no].x,Player[Player_no].y=Player_coordinates[Player_no][index]
        Player_identities[Player_no].update_player_amount(Player_identities[Player_no].get_player_amount()+50)
    else:
        index = Player_coordinates[Player_no].index((Player[Player_no].x,Player[Player_no].y))
        Player[Player_no].x,Player[Player_no].y=Player_coordinates[Player_no][index+Dice_move]


def Pressed_Button(Button_pressed,Player_identities,player_no,Token):
    if (Button_pressed == "BUY") :
        if(Token.get_price() < Player_identities[player_no].get_player_amount()):
            Token.owner_update(player_no)
            Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()-Token.get_price())

def final_winner(purse,Token_list,self):
    for i in range(len(Token_list)):
        if(Token_list[i].get_owner() != None and Token_list[i].get_special_status() == 0):
            purse[Token_list[i].get_owner()] += Token_list[i].get_price()
    max_value = max(purse)
    a=[]
    for i in range(len(purse)):
        if(max_value == purse[i]):
            a.append(self[i])
    winner_text = ""
    if (len(a) == 1):
        winner_text = a[0] +" is the winner"
    else:
        for i in range(len(a)-1):
            if(i == len(a)-2):
                winner_text += a[i] + " and " + a[i+1]+" are the winners"
            else:
                winner_text += a[i]+","
    winner = WINNER_FONT.render(winner_text,True,(0,0,0))
    WIN.blit(winner,(WIDTH//2 - winner.get_width()//2,80))
    pygame.display.update()
    pygame.time.delay(5000)
    pygame.quit()

def main(self):
    run = True
    clock = pygame.time.Clock()
    player_no = 0
    Total_no_of_moves = 250
    total = Button.No_of_players
    Key = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if Key and ROLL_DICE_BUTTON.collidepoint(x, y):
                    roll_dice()
                    Player_movement(Player_rectangles,player_no,Player_Coordinates,current_dice_value)
                    Token = Player_coordinate_assets[player_no][(Player_rectangles[player_no].x,Player_rectangles[player_no].y)]
                    if(Token.get_special_status() == 1):
                        Total_no_of_moves-=1
                        if(Token.get_name() == "Chest"):
                            if(current_dice_value == 1):
                                Player_rectangles[player_no].x,Player_rectangles[player_no].y = Player_Coordinates[player_no][7]
                                Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()-150)
                            elif(current_dice_value == 2):
                                Player_rectangles[player_no].x,Player_rectangles[player_no].y = Player_Coordinates[player_no][14]
                                Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()+150)
                            elif(current_dice_value == 3):
                                Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()+50)
                            elif(current_dice_value == 4):
                                Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()-75)
                            elif(current_dice_value == 5):
                                Player_rectangles[player_no].x,Player_rectangles[player_no].y = Player_Coordinates[player_no][21]
                            else:
                                Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()+25)
                        elif(Token.get_name() == "Crash"):
                            Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()-150)
                        elif(Token.get_name() == "Wind fall"):
                            Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()+150)
                        elif(Token.get_name() == "Closed"):
                            Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount())
                        Key = True
                        player_no += 1
                        player_no=player_no%total
                    elif(Token.get_special_status() == 0):
                        if(Token.get_owner() == player_no):
                            Total_no_of_moves-=1
                            player_no += 1
                            player_no=player_no%total
                        elif(Token.get_owner() == None):
                            Key =False
                        else:
                            Player_identities[player_no].update_player_amount(Player_identities[player_no].get_player_amount()-Token.get_rent())
                            a = Player_identities[Token.get_owner()]
                            a.update_player_amount(Player_identities[Token.get_owner()].get_player_amount()+Token.get_rent())
                            player_no += 1
                            player_no=player_no%total
                            Total_no_of_moves-=1
                elif (not Key) and BUY.collidepoint(x,y):
                    Pressed_Button("BUY",Player_identities,player_no,Token)
                    player_no+=1
                    player_no = player_no % total
                    Total_no_of_moves-=1
                    Key = True
                elif (not Key) and IGNORE.collidepoint(x,y):
                    player_no+=1
                    player_no = player_no % total
                    Key = True
        purse = []
        for i in range(total):
            purse.append(Player_identities[i].get_player_amount())
        draw_window(Player_rectangles,purse,self)
        for i in range(total):
            if (purse[i] <= 0 or Total_no_of_moves <= 0) :
                final_winner(purse,Token_list,self)
    
if __name__ == "__main__":
    main(0)