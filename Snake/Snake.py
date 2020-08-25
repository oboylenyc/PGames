import pygame
import time
import random

pygame.init()

#colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#display
dis_width = 800
dis_height  = 800

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake by Green Island Soft')

#clockset
clock = pygame.time.Clock()

#snake graphics
snake_block = 10
snake_speed = 15

#fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#score display function
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

#highscore display function
def highscore_display(high_score):
    value = score_font.render("High Score: " + str(high_score), True, yellow)
    dis.blit(value, [0, 30])

#get high schore from file function
def get_high_score():
    # Default high score
    high_score = 0
    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.csv", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        #print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")

    return high_score

#save high score to file function
def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.csv", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")

#snake function for display
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#display game over screen function
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#main game function
def main():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        # Get the high score
        high_score = get_high_score()

        while game_close == True:
            dis.fill(blue)
            message("Love you Dani! Press C-Play Again or Q-Quit", red)
            your_score(Length_of_snake - 1)
            highscore_display(high_score)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        highscore_display(high_score)
        # Get the score from the current game
        current_score = 0
        try:
        # Ask the user for his/her score
            current_score = int((Length_of_snake - 1))
        except ValueError:
        # Error, can't turn what they typed into a number
            print("Score Error - Current Score")

        if current_score > high_score:
        # We do! Save to disk
            print("Yea! New high score!")
            save_high_score(current_score)
        else:
            pass

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

main()
