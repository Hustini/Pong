import pygame

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((900, 500))
BG = (000, 000, 000)
clock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption('Pong!')

BRICK_WIGHT, BRICK_HEIGHT = 25, 100
BALL_WIGHT, BALL_HEIGHT = 50, 50
left_brick_image = pygame.image.load('pics/pong_brick.png')
left_brick = pygame.transform.scale(left_brick_image, (BRICK_WIGHT, BRICK_HEIGHT))
right_brick_image = pygame.image.load('pics/pong_brick.png')
right_brick = pygame.transform.scale(right_brick_image, (BRICK_WIGHT, BRICK_HEIGHT))
ball_image = pygame.image.load('pics/pong_ball.png')
pong_ball = pygame.transform.scale(ball_image, (BALL_WIGHT, BALL_HEIGHT))


def draw_window(left, right, ball, score_1, score_2):
    WIN.fill(BG)
    WIN.blit(left_brick, (left.x, left.y))
    WIN.blit(right_brick, (right.x, right.y))
    WIN.blit(pong_ball, (ball.x, ball.y))
    WIN.blit(score_1, (225, 10))
    WIN.blit(score_2, (675, 10))
    pygame.display.update()


def main():
    player_1 = str(0)
    player_2 = str(0)

    left = pygame.Rect(30, 150, BRICK_WIGHT, BRICK_HEIGHT)
    right = pygame.Rect(850, 150, BRICK_WIGHT, BRICK_HEIGHT)
    ball = pygame.Rect(450, 250, BALL_WIGHT, BALL_HEIGHT)

    velocity_ball_x, velocity_ball_y = 5, 5
    velocity_x, velocity_y = 7.5, 7.5

    running = True
    while running:

        font = pygame.font.Font(None, 36)
        score_1 = font.render(player_1, True, (255, 255, 255))
        score_2 = font.render(player_2, True, (255, 255, 255))

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window(left, right, ball, score_1, score_2)

        ball.x += velocity_ball_x
        ball.y += velocity_ball_y

        if ball.right >= 900:
            player_1 = int(player_1) + 1
            player_1 = str(player_1)
            ball = pygame.Rect(450, 250, BALL_WIGHT, BALL_HEIGHT)
        if ball.left <= 0:
            player_2 = int(player_2) + 1
            player_2 = str(player_2)
            ball = pygame.Rect(450, 250, BALL_WIGHT, BALL_HEIGHT)
        if ball.top >= 500:
            velocity_ball_y -= 10
        if ball.bottom <= 0:
            velocity_ball_y += 10

        if ball.colliderect(right):
            velocity_ball_x -= 10
        if ball.colliderect(left):
            velocity_ball_x += 10

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            left.y -= velocity_y
        if keys_pressed[pygame.K_s]:
            left.y += velocity_y
        if keys_pressed[pygame.K_UP]:
            right.y -= velocity_y
        if keys_pressed[pygame.K_DOWN]:
            right.y += velocity_y

        if player_1 == '50':
            running = False

    pygame.quit()
    print(f'Punkte Spieler 1: {player_1}')
    print(f'Punkte Spieler 2: {player_2}')


if __name__ == '__main__':
    main()

"""
dlc ideas:
pawn ball randomizer
bounce randomizer
"""
