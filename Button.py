import pygame
import pygame.font
No_of_players=1
Player_1 = "Jai Shri Ram"
Player_2 = "Jai Shri Krishna"
Player_3 = "OM Namah Sivayah"
Player_4 = "Om namoh venkateshaya"
def create_button(Button_text,Button_x,Button_y,width,height,colour,hover_colour,action,screen,Text_colour):
    mouse_coordinates=pygame.mouse.get_pos()
    tapped = pygame.mouse.get_pressed()[0]
    if(Button_x<mouse_coordinates[0]<Button_x+width and Button_y < mouse_coordinates[1] < Button_y + height):
        pygame.draw.rect(screen,hover_colour,(Button_x,Button_y,width,height))
        if tapped :
            action()
    else:
        pygame.draw.rect(screen,colour,(Button_x,Button_y,width,height))
    font = pygame.font.Font(None,40)
    text_window = font.render(Button_text,True,Text_colour)
    text_rectangle = text_window.get_rect(center = (Button_x + width //2 , Button_y + height//2))
    screen.blit(text_window,text_rectangle)