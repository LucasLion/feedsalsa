import time

from models import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
background = pygame.image.load("assets/background/background.jpg")

food_type = ["fruits", "veggies", "chili"]

fruits_list = pygame.sprite.Group()
veggies_list = pygame.sprite.Group()
chili_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

ADD_FOOD = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_FOOD, 200)

player = Player()
all_sprites_list.add(player)


# Display score
pygame.font.init()
myfont = pygame.font.SysFont("Arial", 30)


def main():
    global score
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == ADD_FOOD:
                new_food = Food(food_type[random.randrange(0, 3)])
                if new_food.type == "fruits":
                    fruits_list.add(new_food)
                    all_sprites_list.add(new_food)
                elif new_food.type == "veggies":
                    veggies_list.add(new_food)
                    all_sprites_list.add(new_food)
                elif new_food.type == "chili":
                    chili_list.add(new_food)
                    all_sprites_list.add(new_food)

        k_pressed = pygame.key.get_pressed()
        player.update(k_pressed)
        fruits_list.update()
        veggies_list.update()
        chili_list.update()

        screen.blit(background, (0, 0))
        for entity in all_sprites_list:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollide(player, fruits_list, dokill=True):
            score += 1
        if pygame.sprite.spritecollide(player, veggies_list, dokill=True):
            score -= 3
        if pygame.sprite.spritecollide(player, chili_list, dokill=True):
            time.sleep(5)
            exit(0)

        if score < 0:
            score = 0
        if score >= 30:
            win_screen = myfont.render("YOU WIN", True, (0, 0, 0))
            width, height = win_screen.get_size()
            screen.blit(win_screen, (SCREEN_WIDTH/2 - width/2, SCREEN_HEIGHT/2 - height/2))

        display_score = myfont.render("SCORE: " + str(score), False, (0, 0, 0))
        screen.blit(display_score, (5, 5))

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
