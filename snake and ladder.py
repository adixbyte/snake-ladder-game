import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 750))
clock = pygame.time.Clock()#this ensures the speed of game is based upon standard clock not based upon user pc speed
running = True
dt = 0

pygame.init()



screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake and Ladder")



font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 30)

WHITE = (255, 255, 255)
BLUE = (0, 0, 0)
GRAY = (220, 220, 220)
GREEN = (100, 255, 100)

screen.fill((255, 255, 255))

user_input_text = ""
number_of_players = 0
game_state = "MENU"
submit_button = pygame.Rect(200, 250, 200, 60)

while game_state == "MENU":
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                
                user_input_text = user_input_text[:-1]
            
            elif event.key == pygame.K_RETURN:
                
                if user_input_text == "1":
                    number_of_players = 1
                elif user_input_text == "2":
                    number_of_players = 2
                elif user_input_text == "3":
                    number_of_players = 3
                elif user_input_text == "4":
                    number_of_players = 4
                else:
                    number_of_players = 1
                    
                game_state = "GAME"
                
            else:
              
                user_input_text += event.unicode

        # Check if clicked the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if submit_button.collidepoint(event.pos):
                
              
                if user_input_text == "1":
                    number_of_players = 1
                elif user_input_text == "2":
                    number_of_players = 2
                elif user_input_text == "3":
                    number_of_players = 3
                elif user_input_text == "4":
                    number_of_players = 4
                else:
                    number_of_players = 1
                    
                game_state = "GAME" 


    if game_state == "MENU":
   
        instruction_text = font.render("Enter players (1, 2, 3, or 4):", True,
        BLUE)
        screen.blit(instruction_text, (130, 50))
        
        hint_text = small_font.render("Anything else will default to 1 player", True, (150, 150, 150))
        screen.blit(hint_text, (125, 90))

        # Draw Text Box (Where i player have to type)
        pygame.draw.rect(screen, GRAY, (200, 150, 200, 50))  # Inside of box
        pygame.draw.rect(screen,
        BLUE, (200, 150, 200, 50), 3) # Border
        
        # Draw the text
        typed_surface = font.render(user_input_text, True,
        BLUE)
        screen.blit(typed_surface, (215, 160))

        # Draw the Start Button
        pygame.draw.rect(screen, GREEN, submit_button)
        pygame.draw.rect(screen,
        BLUE, submit_button, 3) # border
        
        btn_label = font.render("START", True,
        BLUE)
        screen.blit(btn_label, (255, 265))

    pygame.display.flip()


position=1
dice=0

player_positions = [1] * number_of_players# for eg if its 4 then [1,1,1,1]
player_colors = ["red", "blue", "green", "yellow"]
current_player = 0

LADDERS = {2: 38,
4: 14,
9: 31,
21: 42,
28:84,
36:44,
51:67,
71:91,
80:95,
}

SNAKES={16: 6,
47: 26,
49: 11,
56: 46,
62: 19,
64: 60,
87: 24,
93: 73,
96: 75,
98: 78
}

box_side=50
gap=3
start_x,start_y=50,50

button_rect = pygame.Rect(400, 700, 120, 50)

def draw_dice(screen, x, y, size, value):
    border_radius = size // 10

    pygame.draw.rect(screen, "white", (x, y, size, size), border_radius=border_radius)
    pygame.draw.rect(screen, "black", (x, y, size, size), width=3, border_radius=border_radius)

    dot_radius = size // 10
    padding = size // 4


    center = (x + size // 2, y + size // 2)
    top_left = (x + padding, y + padding)
    top_right = (x + size - padding, y + padding)
    bottom_left = (x + padding, y + size - padding)
    bottom_right = (x + size - padding, y + size - padding)
    middle_left = (x + padding, y + size // 2)
    middle_right = (x + size - padding, y + size // 2)


    dot_positions = []

    if value == 1:
        dot_positions = [center]
    elif value == 2:
        dot_positions = [top_left, bottom_right]
    elif value == 3:
        dot_positions = [top_left, center, bottom_right]
    elif value == 4:
        dot_positions = [top_left, top_right, bottom_left, bottom_right]
    elif value == 5:
        dot_positions = [top_left, top_right, center, bottom_left, bottom_right]
    elif value == 6:
        dot_positions = [top_left, top_right, middle_left, middle_right, bottom_left, bottom_right]


    for pos in dot_positions:
        pygame.draw.circle(screen, "black", pos, dot_radius)


def player_position(player_position, color):
    x=start_x
    y=start_y
    a=(player_position-1)

    if (10-a//10)%2!=0:
        x=start_x+53*(9-(a%10))
    else:
        x=start_x+53*(a%10)
    y=start_y+53*(9-a//10)
    pygame.draw.circle(screen, color,(x + box_side / 2, y + box_side / 2),15)
    return (x + box_side / 2, y + box_side / 2)


def coordinate(player_position):
    x=start_x
    y=start_y
    a=(player_position-1)

    if (10-a//10)%2!=0:
        x=start_x+53*(9-(a%10))
    else:
        x=start_x+53*(a%10)

    y=start_y+53*(9-a//10)

    return (x + box_side / 2, y + box_side / 2)


pygame.display.set_mode((800, 800))

while running:
    for event in pygame.event.get():#to call event in pygame
        if event.type == pygame.QUIT:#in case it wants to exit
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                position = player_positions[current_player]

                dice = random.randint(1, 6)
                new_position = position + dice

                if new_position <= 100:
                    position = new_position

                if position in LADDERS:
                    position = LADDERS[position]
                elif position in SNAKES:
                    position = SNAKES[position]

                player_positions[current_player] = position

                print("ROLL")


                print("Player:", current_player + 1)
                print("Dice:", dice)
                print("Position:",position)

                current_player += 1

                if current_player == number_of_players:
                    current_player = 0

            else:
                print("try next time")


        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if button_rect.collidepoint(mouse_x, mouse_y):

                position = player_positions[current_player]

                dice = random.randint(1, 6)
                new_position = position + dice

                if new_position <= 100:
                    position = new_position
                if position in LADDERS:
                    position = LADDERS[position]
                elif position in SNAKES:
                    position = SNAKES[position]

                player_positions[current_player] = position

                print("ROLL")
                print("Player:", current_player + 1)
                print("Dice:", dice)
                print("Position:",position)

                current_player += 1

                if current_player == number_of_players:
                    current_player = 0


    screen.fill("purple")


    y=start_y
    number=100
    font=pygame.font.Font(None,30)
    for i in range(1,11):
        x=start_x
        if i%2==1:
            for j in range(1,11):
                pygame.draw.rect(screen,"white",(x,y,box_side,box_side))
                text=font.render(str(number),True,"black")
                screen.blit(text,(15+x,15+y))
                number-=1
                pygame.draw.rect(screen,"grey",(x,y,box_side,box_side),4)
                x+=box_side+gap
            y+=box_side+gap

        else:
            for j in range(1,11):
                pygame.draw.rect(screen,"white",(x,y,box_side,box_side))
                text=font.render(str(number-9),True,"black")
                screen.blit(text,(15+x,15+y))
                number+=1
                pygame.draw.rect(screen,"grey",(x,y,box_side,box_side),4)
                x+=box_side+gap
            y+=box_side+gap
            number-=20


    for current_player_position in range(number_of_players):
        player_position(player_positions[current_player_position], player_colors[current_player_position])


    for start, end in LADDERS.items():

        start_coords = coordinate(start)
        end_coords =coordinate(end)
        shifted_start_coords = (start_coords[0] + 15, start_coords[1])
        shifted_end_coords = (end_coords[0] + 15, end_coords[1])
        pygame.draw.line(screen,"brown",shifted_start_coords,shifted_end_coords,3)
        pygame.draw.line(screen, "brown", start_coords, end_coords, 3)

        steps = max(abs(end - start) // 5, 3)#gives absolute value then comapres for maximum with 3 so that atleast 3 steps are there

        for j in range(1, steps + 1):

            t = j / (steps + 1)

            x1 = start_coords[0] + t * (end_coords[0] - start_coords[0])
            y1 = start_coords[1] + t * (end_coords[1] - start_coords[1])

            x2 = shifted_start_coords[0] + t * (shifted_end_coords[0] - shifted_start_coords[0])
            y2 = shifted_start_coords[1] + t * (shifted_end_coords[1] - shifted_start_coords[1])

            pygame.draw.line(screen, "black", (x1, y1), (x2, y2), 3)


    for head, tail in SNAKES.items():

        start_coords = coordinate(head)
        end_coords =coordinate(tail)

        pygame.draw.circle(screen, "yellow",(start_coords),10)
        pygame.draw.line(screen, "red", start_coords, end_coords, 3)


    pygame.draw.rect(screen, "blue", button_rect)
    text=font.render("ROLL",True,"black")
    screen.blit(text,(415,715))


    draw_dice(screen, 600, 650, 100, dice)


    pygame.display.flip()

pygame.quit()
sys.exit()